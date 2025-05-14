d, MOD = map(int, input().split())

dp = [[0] * (d + 1) for _ in range(d + 1)]

dp[0][0] = 1
dp[1][1] = 1

for i in range(2, d):
    dp[i][1] += dp[i - 1][2]

    for j in range(2, d + 1):
        dp[i][j] += dp[i - 1][j - 1]
        if j != d:
            dp[i][j] += dp[i - 1][j + 1]

        dp[i][j] %= MOD

print(dp[d - 1][1])
