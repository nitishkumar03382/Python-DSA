"""
INPUT: n = 5
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
def print_pattern(n):
    for i in range(n):
        start = 1
        if i % 2 == 1:
            start = 0
        for j in range(i+1):
            if j % 2 == 0:
                print(start, end = ' ', sep = ' ')
            else:
                if start == 0:
                    print(1, end = ' ', sep = ' ')
                elif start == 1:
                    print(0, end = ' ', sep = ' ')
        print()
if __name__ == '__main__':
    n = int(input())
    print_pattern(n)