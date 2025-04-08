import sys

input = sys.stdin.readline
MOD = 1_000_000_007

N, K = map(int, input().split())
target = list(map(int, input().split()))
pow2 = [1] * (N + 2)
for i in range(1, N + 2):
    pow2[i] = (pow2[i - 1] * 2) % MOD

ans = 0
cur_K = K

for i in range(N, 0, -1):
    a_i = target[i - 1]
    if a_i == cur_K:
        continue
    else:
        ans = (ans + pow2[i - 1]) % MOD
        cur_K = 6 - cur_K - a_i

print(ans)
