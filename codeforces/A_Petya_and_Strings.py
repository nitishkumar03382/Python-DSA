if __name__ == '__main__':
    w1 = input()
    w2 = input()
    w1 = w1.lower()
    w2 = w2.lower()
    if w1 == w2:
        print(0)
    elif w1 < w2:
        print(-1)
    else:
        print(1)
    