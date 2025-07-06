def solve(n):
    if n <= 3:
        return 0

    if n % 2 == 0:
        return n * (n - 4) // 2 + 1
    else:
        return n * (n - 3) // 2


T = int(input())

for _ in range(T):
    N = int(input())
    print(solve(N))