class stack:
    
    def __init__(self, size) -> None:
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def push(self,e):
        self.top += 1
        if self.top == self.size:
            print('Stack size is Full')
        else:
            self.arr[self.top] = e
            print(e, 'pushed to stack')
    def pop(self):
        if self.top == -1:
            print('Stack is empty')
        else:
            print(self.arr[self.top], 'is popped')
            self.arr[self.top] = None
            self.top -= 1
    def peek(self):
        if self.top == -1:
            print(None)
        else:
            print(self.arr[self.top])
    def empty(self):
        if self.top == -1:
            print('Yes')
        else:
            print('No')



if __name__ == '__main__':
    st = stack(5)
    st.empty()
    st.push(1)
    st.push(2)
    st.peek()
    st.push(3)
    st.empty()
    st.pop()
    st.pop()
    st.pop()
    st.push(11)
    st.empty()
    st.peek()
    st.push(5)
    st.push(5)
    st.push(5)
    st.push(5)
    st.push(5)
