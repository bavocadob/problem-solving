import sys

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    a, b, c = map(int, input().split())
    if ((a & 1) + (b & 1) + (c & 1)) & 1:
        print('NO')
    else:
        print('YES')
