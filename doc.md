# Django To-Do App Documentation

This document provides a detailed guide for developing a Django-based To-Do app with user authentication, session management, and cookie handling. Follow along to build and understand the app.

---

## 1. Project Setup

### Prerequisites

- Python 3.x installed
- Django installed (`pip install django`)
- Basic understanding of Django project structure

### Create a Django Project

1. Create a new Django project:
   ```bash
   django-admin startproject todo_project
   ```
2. Navigate to the project directory:
   ```bash
   cd todo_project
   ```
3. Create a new app:
   ```bash
   python manage.py startapp todo
   ```
4. Add the `todo` app to the `INSTALLED_APPS` in `todo_project/settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       'todo',
   ]
   ```

---

## 2. Models

### Define Models in `todo/models.py`

```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### Migrate Database

1. Create migrations:
   ```bash
   python manage.py makemigrations
   ```
2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

---

## 3. User Authentication

### Setup Authentication Views

Django provides built-in views for authentication. Update `todo_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('todo.urls')),
]
```

### Create `todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]
```

### User Registration View

Add a registration form in `todo/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

Create a template for registration at `todo/templates/registration/register.html`:

```html
{% extends 'base.html' %}

{% block content %}
<h2>Register</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
{% endblock %}
```

---

## 4. To-Do App Views

### Display Tasks

Add a view to display tasks in `todo/views.py`:

```python
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/index.html', {'tasks': tasks})
```

Create a template at `todo/templates/todo/index.html`:

```html
{% extends 'base.html' %}

{% block content %}
<h2>Your Tasks</h2>
<ul>
    {% for task in tasks %}
    <li>
        <input type="checkbox" {% if task.completed %}checked{% endif %}>
        {{ task.title }}
        <a href="{% url 'delete_task' task.id %}">Delete</a>
    </li>
    {% endfor %}
</ul>
<a href="{% url 'create_task' %}">Add Task</a>
{% endblock %}
```

### Add, Toggle, and Delete Tasks

Add views in `todo/views.py`:

```python
from django.shortcuts import get_object_or_404

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(user=request.user, title=title)
        return redirect('index')
    return render(request, 'todo/create_task.html')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('index')

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('index')
```

Templates for `create_task`:

```html
{% extends 'base.html' %}

{% block content %}
<h2>Add Task</h2>
<form method="post">
    {% csrf_token %}
    <input type="text" name="title" placeholder="Task title">
    <button type="submit">Add</button>
</form>
{% endblock %}
```

---

## 5. Session and Cookies Handling

### Enable Sessions

Ensure sessions are enabled in `settings.py`:

```python
MIDDLEWARE = [
    ...,
    'django.contrib.sessions.middleware.SessionMiddleware',
]
```

### Use Sessions

Store a user preference in a session (e.g., theme preference):

```python
def set_theme(request):
    theme = request.GET.get('theme', 'light')
    request.session['theme'] = theme
    return redirect('index')
```

### Access Cookies

Set and read cookies in views:

```python
def set_cookie(request):
    response = redirect('index')
    response.set_cookie('favorite_color', 'blue')
    return response

def get_cookie(request):
    color = request.COOKIES.get('favorite_color', 'not set')
    return render(request, 'todo/cookie.html', {'color': color})
```

Template for `cookie.html`:

```html
{% extends 'base.html' %}

{% block content %}
<p>Your favorite color is: {{ color }}</p>
{% endblock %}
```

---

## 6. Testing and Running

1. Run the development server:
   ```bash
   python manage.py runserver
   ```
2. Visit `http://127.0.0.1:8000/` to access the app.

---

## 7. Additional Features

- Add task prioritization.
- Integrate a search feature.
- Use Django REST framework for an API backend.
- Enhance the UI with JavaScript and CSS frameworks.

