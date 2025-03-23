import sys

input = sys.stdin.readline
MOD = 1000000007

n, m, k = map(int, input().split())

ans = 0

if k > n:
    ans = pow(m, n, MOD)
elif k == n:
    ans = pow(m, (k + 1) // 2, MOD)
else:
    if k == 1:
        ans = pow(m, n, MOD)
    elif k == 2:
        ans = m
    else:
        ans = (m * m) % MOD if k % 2 == 1 else m % MOD

print(ans)
