"""
INPUT: n = 4
D
DC
DCB
DCBA
"""
def print_pattern(n):
    c = 65 + n - 1
    for i in range(n):
        for j in range(i + 1):
            print(chr(c - j), end = '')
            # c += 1
        print()
        

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)