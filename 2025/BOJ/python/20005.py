import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(bx, by):
    dist_map = [[-1] * M for _ in range(N)]
    q = deque([(bx, by)])
    dist_map[bx][by] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] and dist_map[nx][ny] == -1:
                dist_map[nx][ny] = dist_map[x][y] + 1
                q.append((nx, ny))

    return dist_map


N, M, P = map(int, input().split())
field = []
users = []
boss_index = (-1, -1)

for i in range(N):
    line = input().rstrip()
    row = []
    for j, ch in enumerate(line):
        if ch == 'X':
            row.append(False)
        else:
            row.append(True)
            if ch == 'B':
                boss_index = (i, j)
            elif ch.isalpha():
                users.append((i, j, ch))
    field.append(row)

damages = {}
for _ in range(P):
    player, dmg = input().split()
    damages[player] = int(dmg)

boss_hp = int(input())

bx, by = boss_index
dist_map = bfs(bx, by)

user_queue = []
for x, y, name in users:
    d = dist_map[x][y]
    if d != -1:
        user_queue.append((d, name))

user_queue.sort(reverse=True)

cur_time = 0
cur_dps = 0
cur_damaged = 0
ans = 0

while user_queue:
    time, user = user_queue.pop()

    if time > cur_time:
        cur_damaged += (time - cur_time - 1) * cur_dps

        if cur_damaged >= boss_hp:
            break

        cur_damaged += cur_dps

    cur_damaged += damages[user]
    cur_dps += damages[user]
    cur_time = time
    ans += 1

print(ans)
