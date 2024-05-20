if __name__ == '__main__':
    t = int(input())
    while t > 0:
        w = input()
        if len(w) > 10:
            n = len(w) - 2
            ans = w[0] + str(n) + w[-1]
            print(ans)
        else:
            print(w)
        t -= 1
    