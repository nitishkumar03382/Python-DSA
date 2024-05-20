if __name__ == '__main__':
    s = input()
    vowels = 'aAeEiIoOuUyY'
    ans = ""
    for ch in s:
        if ch in vowels:
            ...
        else:
            ans += '.' + ch.lower()
    print(ans)