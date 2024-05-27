from math import log
def is_armstrong(n):
    num_dig = int(log(n, 10)) + 1
    # print(num_dig)
    sum_num = 0
    c = n
    while n:
        d = n % 10
        sum_num += d ** num_dig
        n = n // 10
        # print(sum_num)
    return c == sum_num
res = is_armstrong(1)
print(res)
