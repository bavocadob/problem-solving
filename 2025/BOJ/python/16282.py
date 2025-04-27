import sys


def solve(n):
    i = 0
    while True:
        if (i + 1) * (1 << (i + 1)) - 1 >= n:
            return i
        i += 1


N = int(sys.stdin.readline().strip())
print(solve(N))
