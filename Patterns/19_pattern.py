"""
INPUT: n = 4
********
***  ***
**    **
*      *
**    **
***  ***
********
"""
def print_pattern(n):
    for i in range((2 * n) - 1):
        if i < n:
            for j in range(2 * n):
                if j < n - i:
                    print('*', end = '')
                elif j >= n + i:
                    print('*', end = '')
                else:
                    print(' ', end = '')
        else:
            for j in range(2 * n):
                if j < n - i:
                    print('*', end = '')
                elif j >= n + i:
                    print('*', end = '')
                else:
                    print(' ', end = '')

        print()
        

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)