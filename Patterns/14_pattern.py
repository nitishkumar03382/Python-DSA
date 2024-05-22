"""
INPUT: n = 4
A
AB
ABC
ABCD
"""
def print_pattern(n):
    c = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(c+j), end = '')
        print()
        

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)