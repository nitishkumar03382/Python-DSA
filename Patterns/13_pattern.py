"""
INPUT: n = 4
1
2 3
4 5 6
7 8 9 10
"""
def print_pattern(n):
    counter = 1
    for i in range(n):
        for j in range(i + 1):
            print(counter, end = ' ')
            counter += 1
        print()

if __name__ == '__main__':
    n = int(input())
    print_pattern(n)