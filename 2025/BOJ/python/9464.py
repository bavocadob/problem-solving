import math
import sys

input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


pairs = []
max_L = 1_000_000

for x in range(1, int(math.sqrt(max_L))):
    for y in range(1, x):
        if gcd(x, y) == 1 and (x - y) % 2 == 1:
            w = 2 * x * y
            h = x * x - y * y
            if w > h:
                w, h = h, w
            if w + h >= max_L // 2:
                break
            pairs.append((w, h))

pairs.sort(key=lambda p: p[0] + p[1])

prefix_sum = [0]
for x, y in pairs:
    temp = prefix_sum[-1] + 2 * (x + y)
    prefix_sum.append(temp)
    if prefix_sum[-1] > max_L:
        break

T = int(input())


def solve(size):
    l, r = 0, len(prefix_sum) - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if prefix_sum[mid] <= size:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


for _ in range(T):
    L = int(input())
    print(solve(L))
