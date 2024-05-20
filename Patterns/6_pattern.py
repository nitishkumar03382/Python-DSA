"""
Input: n = 4
1 2 3 4
1 2 3
1 2
1
----------------
Input n = 2
1 2
1
"""
def print_pattern(n):
    for i in range(n):
        for j in range( n - i):
            print(j + 1, end = ' ')
        if i < n -1:
            print()

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)