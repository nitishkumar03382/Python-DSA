def mySqrt(x):
    s = 0
    e = x
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2

        if mid * mid > x:
            e = mid - 1
        elif mid * mid < x:
            ans = mid
            s = mid + 1
        else:
            return mid
    return ans

if __name__ == '__main__':
    print(mySqrt(99))
        