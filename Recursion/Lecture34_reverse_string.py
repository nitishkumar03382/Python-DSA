def swap(a, b):
    tmp = a
    a = b
    b = tmp
def rev(s, i, j):
    if(i > j):
        return
    s[i], s[j] = s[j], s[i]
    rev(s, i+1, j-1)
    # return s

    

if __name__ == '__main__':
    # s = list("helloWorld")
    # s = list("a")
    s = list("")

    rev(s, 0, len(s) - 1)
    print("".join(s))