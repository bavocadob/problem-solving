import sys

input = sys.stdin.readline
MOD = 10 ** 9 + 7

n, k = map(int, input().split())

_ = input()

kk = k
if k > n - k:
    k = n - k
num = 1
den = 1

for i in range(1, k + 1):
    num = num * (n - i + 1) % MOD
    den = den * i % MOD
c = num * pow(den, MOD - 2, MOD) % MOD
ans = c * pow(2, kk - 1, MOD) % MOD
print(ans)
