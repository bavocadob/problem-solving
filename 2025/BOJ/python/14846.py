import sys

input = sys.stdin.readline

N = int(input())
A = [[0] * (N + 1)]
for _ in range(N):
    A.append([0] + list(map(int, input().split())))

p_sum = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(11)]

for k in range(1, 11):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            p_sum[k][i][j] = p_sum[k][i - 1][j] + p_sum[k][i][j - 1] - p_sum[k][i - 1][j - 1]

            if A[i][j] == k:
                p_sum[k][i][j] += 1

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())

    ans = 0
    for k in range(1, 11):
        exist = p_sum[k][x2][y2] - p_sum[k][x1 - 1][y2] - p_sum[k][x2][y1 - 1] + p_sum[k][x1 - 1][y1 - 1]

        if exist:
            ans += 1

    print(ans)
