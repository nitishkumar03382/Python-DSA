# You are at 0th stair and you have to climb to nth stair
# Two possible ways to climb stair one or two step at a time
# find total number of ways to climb the stair
def climb_stairs(n):
    if n < 0:
        return 0;
    if n == 0:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)
if __name__ == '__main__':
    n = int(input())
    ans = climb_stairs(n)
    print(ans)