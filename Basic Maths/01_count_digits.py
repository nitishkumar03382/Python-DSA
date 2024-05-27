from math import log
def count_digits(n):
    c = 0
    if n == 0:
        return 1
    while n:
        n = n // 10
        c += 1
    return c
def count_digits_optimal(n):
    return int(log(n, 10)) + 1

if __name__ == '__main__':
    num_digits = count_digits_optimal(9090)
    print(num_digits)
