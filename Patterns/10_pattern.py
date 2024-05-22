"""
INPUT: n = 5
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
def print_pattern(n):
    for i in range(n):
        print('* ' * (i + 1))
    for i in range(n-1, 0, -1):
        print('* ' * i)
if __name__ == '__main__':
    n = int(input())
    print_pattern(n)