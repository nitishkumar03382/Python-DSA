if __name__ == '__main__':
    num_coins = int(input())
    coin_ip = input().split()
    coins = []
    for i in range(num_coins):
        coin = int(coin_ip[i])
        coins.append(coin)
    coins.sort(reverse=True)
    sum_coins = sum(coins)
    ans = 0
    curr = 0
    i = 0
    while curr <= sum_coins // 2:
        curr += coins[i]
        i += 1
        ans += 1
    print(ans)
