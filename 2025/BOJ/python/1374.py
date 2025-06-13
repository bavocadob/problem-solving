import heapq
import sys

input = sys.stdin.readline
N = int(input())

lectures = []
for _ in range(N):
    _, s, e = map(int, input().split())
    lectures.append((s, e))

lectures.sort()

queue = []

for start, end in lectures:
    if queue and queue[0] <= start:
        heapq.heappop(queue)
    heapq.heappush(queue, end)

print(len(queue))
