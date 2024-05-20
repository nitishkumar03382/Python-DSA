def is_possible_solution(books, num_books, num_students, pages):
    std_cnt = 1
    page_sum = 0
    for p in books:
        if p + page_sum <= pages:
            page_sum += p
        else:
            std_cnt += 1
            if std_cnt > num_students or p > pages:
                return False
            page_sum = p
    return True
    

def allocate_pages(books, num_books, num_students):
    total_pages = sum(books)
    s, e = 0, total_pages
    s_count = 1
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if is_possible_solution(books, num_books, num_students, mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans



    return total_pages

if __name__ == '__main__':
    books = [10, 20, 30, 40]
    num_students = 2
    ans = allocate_pages(books, len(books), num_students)
    print(ans)