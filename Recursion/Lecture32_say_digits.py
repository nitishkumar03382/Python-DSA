# IP = 301            |  1134
# OP = Three zero one |  One one three four
# The first letter of first word should always be in Capital
numbers = ['zero', 'one', 'two', 
           'three', 'four', 'five', 'six',
           'seven', 'eight', 'nine']
def say_digits(n):
    if n == 0:
        return
    say_digits(n // 10)
    digit = numbers[n % 10]
    if n // 10 == 0:
        print(digit.capitalize(), end=' ')
    else:
        print(digit, end=' ')

if __name__ == '__main__':
    n = int(input())
    say_digits(n)