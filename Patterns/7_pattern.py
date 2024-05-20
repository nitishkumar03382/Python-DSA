"""
INPUT: n = 5
    *
   ***
  *****
 *******
*********
"""
def print_pattern(n):
    for i in range(n):
        # Print Spaces
        for j in range(n - i - 1):
            print(' ', end = '')
        for j in range(2 * i + 1):
            print('*', end = '')
        print()
if __name__ == '__main__':
    n = int(input())
    print_pattern(n)