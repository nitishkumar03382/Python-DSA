def print_counting(n):
    if n == 0:
        return;
    print_counting(n-1)
    print(n)
def print_counting_reverse(n):
    if n == 0:
        return;
    print(n)
    print_counting_reverse(n-1)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print("1 to n:")
    print_counting(n)
    print("n to 1:")
    print_counting_reverse(n)