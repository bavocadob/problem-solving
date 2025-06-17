import sys

ipnut = sys.stdin.readline
N, M = map(int, input().split())

heights = list(map(int, input().split()))

pref = [0] * (N + 1)
for _ in range(M):
    l, r, height = map(int, input().split())

    pref[l - 1] += height
    pref[r] -= height

heights[0] += pref[0]
for i in range(1, N + 1):
    pref[i] += pref[i - 1]
    if i < N:
        heights[i] += pref[i]

print(*heights)
