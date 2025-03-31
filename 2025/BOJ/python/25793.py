import sys

input = sys.stdin.readline


def solve(r, c):
    m, n = max(r, c), min(r, c)
    k = m - n

    white = n * (n + 1) * (2 * n + 1) // 3 - n * (n + 1) + n * (n + 1) * k - n * k + n
    black = n * (n + 1) * (2 * n + 1) // 3 - n * (n + 1) + n * (n + 1) * k - n * k

    return white, black


T = int(input())

for _ in range(T):
    R, C = map(int, input().split())
    print(*solve(R, C))
