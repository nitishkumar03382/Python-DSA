def reverse_dig(n):
    # n = 123
    rev = 0
    while n:
        rev = (rev * 10) + n % 10
        n = n // 10
    return rev
if __name__ == '__main__':
    ans = reverse_dig(120300)
    print(ans)