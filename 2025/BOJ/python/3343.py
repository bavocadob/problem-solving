import math

N, A, B, C, D = map(int, input().split())

if B * C < D * A:
    A, B, C, D = C, D, A, B

min_cost = float('inf')

for i in range(C):
    remain = N - i * A
    temp = math.ceil(remain / C) if remain > 0 else 0
    total = i * B + temp * D
    min_cost = min(min_cost, total)
    if temp == 0: break
print(min_cost)
