import sys

input = sys.stdin.readline


def solve():
    a, b, c, d = map(int, input().split())
    dp = [0] * 2_000_001
    dp[0] = 1

    for coin in [a, b, c, d]:
        for i in range(coin, 2_000_001):
            if dp[i - coin]:
                dp[i] = 1

    print(1000000 - sum(dp[:1_000_001]) + 1)

    for i in range(2_000_000, -1, -1):
        if dp[i] == 0:
            if i <= 1_000_000:
                print(i)
            else:
                print(-1)
            break


T = int(input())

for _ in range(T):
    solve()
