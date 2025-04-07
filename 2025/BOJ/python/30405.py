import sys

input = sys.stdin.readline
N, M = map(int, input().split())

gate = []
for _ in range(N):
    temp = list(map(int, input().split()))
    gate.append(temp[1])
    gate.append(temp[-1])

gate.sort()

print(gate[N])
