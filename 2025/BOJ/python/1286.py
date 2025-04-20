import sys

input = sys.stdin.readline
n, m = map(int, input().split())
rect = []
dp = [[0] * (m * 2) for _ in range(n * 2)]
ans = [0] * 26

for i in range(n):
    s = input().strip()

    rect.append(list(s + s))

for i in range(n):
    rect.append(rect[i])

for i in range(n * 2):
    for j in range(m * 2):
        dp[i][j] = (i + 1) * (j + 1) * (n * 2 - i) * (m * 2 - j)

for i in range(n * 2):
    for j in range(m * 2):
        ans[ord(rect[i][j]) - ord('A')] += dp[i][j]

for num in ans:
    print(num)
