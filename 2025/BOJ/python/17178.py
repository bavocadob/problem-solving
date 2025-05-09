import sys

input = sys.stdin.readline


def solve():
    waiting = []
    cur = 0
    while queue or waiting:
        if queue and queue[-1] == fan_rank[cur]:
            queue.pop()
            cur += 1
            continue

        if waiting and waiting[-1] == fan_rank[cur]:
            waiting.pop()
            cur += 1
            continue

        if queue:
            waiting.append(queue.pop())
        else:
            break

    return cur == len(fan_rank)


N = int(input())

queue = []

for _ in range(N):
    queue += list(input().split())

fan_rank = sorted(queue, key=lambda x: (x.split('-')[0], int(x.split('-')[1])))
queue = list(reversed(queue))

print('GOOD' if solve() else 'BAD')
