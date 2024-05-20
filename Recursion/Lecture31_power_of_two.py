def power_of_two(power):
    if power == 0:
        return 1
    return 2 * power_of_two(power - 1)

if __name__ == '__main__':
    power = int(input("Enter the power of 2: "))
    ans = power_of_two(power)
    print("2 ^", power, "=", ans)