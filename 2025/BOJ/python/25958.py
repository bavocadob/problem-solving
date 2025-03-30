N, K = map(int, input().split())

coins = []

for i in range(1, N + 1):
    temp = 0
    cur = i

    while cur:
        temp += cur % 10
        cur //= 10

    if i % temp == 0:
        coins.append(i)

dp = [0] * (N + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, N + 1):
        dp[i] += dp[i - coin]
        dp[i] %= K

print(dp[N])
