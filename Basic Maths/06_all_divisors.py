from math import sqrt
def all_divisors(n):
    ans = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    return ans
print(all_divisors(35))

