import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def is_valid(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


def main():
    N, M = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(N)]

    a = (-1, -1)
    b = (-1, -1)

    for i in range(N):
        for j in range(M):
            if board[i][j] != 'o':
                continue
            board[i][j] = '.'
            if a == (-1, -1):
                a = (i, j)
            else:
                b = (i, j)

    visited = set()
    visited.add((a[0], a[1], b[0], b[1]))
    q = deque()

    q.append((0, a[0], a[1], b[0], b[1]))

    while q:
        dist, ax, ay, bx, by = q.popleft()
        if dist >= 10:
            break

        for k in range(4):
            nax, nay = ax + dx[k], ay + dy[k]
            nbx, nby = bx + dx[k], by + dy[k]
            a_valid = is_valid(N, M, nax, nay)
            b_valid = is_valid(N, M, nbx, nby)
            if (a_valid and not b_valid) or (not a_valid and b_valid):
                print(dist + 1)
                return
            elif not a_valid or not b_valid:
                continue

            if board[nax][nay] == '#':
                nax, nay = ax, ay

            if board[nbx][nby] == '#':
                nbx, nby = bx, by

            if (nax, nay, nbx, nby) in visited:
                continue

            visited.add((nax, nay, nbx, nby))
            q.append((dist + 1, nax, nay, nbx, nby))

    print(-1)


if __name__ == '__main__':
    main()
