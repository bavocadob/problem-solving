import sys

input = sys.stdin.readline
dx = [1, 0]
dy = [0, 1]

from collections import deque

N = int(input())

A = [list(input().rstrip()) for _ in range(N)]

q = deque()
q.append((0, 0, A[0][0]))

front = set()
back = set()
while q:
    x, y, s = q.popleft()
    if len(s) == N:
        front.add((s, x, y))
        continue
    elif len(s) == N + 1:
        break

    for k in range(2):
        nx, ny = x + dx[k], y + dy[k]

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        q.append((nx, ny, s + A[nx][ny]))

del q

q = deque()
q.append((N - 1, N - 1, A[N - 1][N - 1]))

while q:
    x, y, s = q.popleft()
    if len(s) == N:
        back.add((s, x, y))
        continue

    for k in range(2):
        nx, ny = x + dx[k] * - 1, y + dy[k] * - 1

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        q.append((nx, ny, s + A[nx][ny]))

ans = 0
ans_set = set()

for s, x, y in front:
    if s in ans_set:
        continue

    if (s, x, y) in back:
        ans_set.add(s)
        ans += 1

print(ans)
