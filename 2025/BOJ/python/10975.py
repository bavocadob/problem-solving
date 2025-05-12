import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
    num = int(input())
    arr.append((num, i))

arr.sort()

orders = [0] * N

for i in range(N):
    _, order = arr[i]
    orders[order] = i

deques = []

for order in orders:
    for q in deques:
        if q[0] == order + 1:
            q.appendleft(order)
            break
        elif q[-1] == order - 1:
            q.append(order)
            break
    else:
        temp = deque()
        temp.append(order)
        deques.append(temp)

print(len(deques))
