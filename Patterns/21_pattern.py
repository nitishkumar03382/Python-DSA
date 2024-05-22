"""
INPUT: n = 4
****

*  *

*  *

****

"""
def print_pattern(n):
    border = '*' + (' ' * (n - 2)) + '*'
    for i in range(2*n):
        if i == 0 or i == 2*n - 1:
            print('*' * n)
        elif i % 2 == 0:
            print(border)
        # print()
        

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)