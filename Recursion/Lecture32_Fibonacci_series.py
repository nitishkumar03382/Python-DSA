# 0,   1,  1,  2, 3, 5, 8, 13, 21
# 0th 1st 2nd 3rd, ...
# find the nth fibonacci number
def fibonacci(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = int(input())
    ans = fibonacci(n)
    print(ans)