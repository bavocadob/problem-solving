import math

ans = 0
N = int(input())

x = int(math.isqrt(N))

for i in range(1, x):
    ans += i ** 2

cur = 0

for _ in range(N - (x ** 2)):
    ans += cur
    cur += 1
    cur %= x

print(ans)
