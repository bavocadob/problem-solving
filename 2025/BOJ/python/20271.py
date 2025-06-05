import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k1, alpha = map(int, input().split())

    visited = set()
    cur = k1
    count = 0

    while True:
        if cur in visited:
            break

        visited.add(cur)
        count += 1

        if count == n:
            break

        next_val = (k1 + alpha * (cur * cur)) % n
        cur = next_val

    print(count)
