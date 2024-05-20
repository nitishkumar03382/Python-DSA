if __name__ == '__main__':
    num = int(input())
    x = num
    flag = True
    while x > 0:
        if x % 10 not in[4,7]:
            flag = False
            break
        x = x // 10
    if flag == False and (num % 7 == 0 or num % 4 == 0):
        flag = True
    elif flag == False:
        

    if flag:
        print('Yes')
    else:
        print('No')
        