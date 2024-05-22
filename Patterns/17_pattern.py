"""
INPUT: n = 4
   A
  ABA
 ABCBA
ABCDCBA
"""
def print_pattern(n):
    for i in range(n):
        c = 65
        print(' ' * (n - i - 1), end = '')
        for j in range(i + 1):
            print(chr(c), end = '')
            c += 1

        c -= 2

        for j in range(i):
            print(chr(c), end = '')
            c -= 1
        print()
        

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)