"""
INPUT: n = 4
1      1
12    21
123  321
12344321
"""
def print_pattern(n):
    for i in range(n):
      for j in range(2*n):
         if j <= i:
            print(j+1, end = '')  
         elif j >= (2 * n) - (i+1):
            print((2*n) - j, end = '')
         else:
            print(' ', end = '')

      print()
if __name__ == '__main__':
    n = int(input())
    print_pattern(n)