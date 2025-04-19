import math


def solve(N, K):
    if K > N // 2:
        K = N - K

    d = math.gcd(N, K)

    if d != 1:
        N //= d
        K //= d

    return N * (K - 1)


n, k = map(int, input().split())
print(solve(n, k))
