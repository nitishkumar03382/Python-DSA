def reverse_dig(n):
    # n = 123
    rev = 0
    while n:
        rev = (rev * 10) + n % 10
        n = n // 10
    return rev
if __name__ == '__main__':
    num = 1
    ans = reverse_dig(num) == num
    print(ans)