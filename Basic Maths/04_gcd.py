def gcd1(a, b):
    if a < b:
        a,b = b,a
    # 25,10 => 10, 5 => 5, 0
    # 13,7 => 7, 6 => 6, 1 => 1, 0
    while b:
        rem = a % b
        a = b
        b = rem
    return a
g1 = gcd1(380, 760)
print(g1)