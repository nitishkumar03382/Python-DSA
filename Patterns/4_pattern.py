"""
Input: n = 4
1
2 2
3 3 3
4 4 4 4
----------------
Input n = 2
1
2 2
"""
def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(i + 1, end = ' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)