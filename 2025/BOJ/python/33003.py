import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def main():
    N, M = map(int, input().split())

    circuit = [list(input().strip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M

    def dfs(x, y):
        visited[x][y] = True
        val = circuit[x][y]

        if val.isdigit():
            return int(val)

        child_values = []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not is_valid(nx, ny) or visited[nx][ny] or circuit[nx][ny] == '.':
                continue

            child_values.append(dfs(nx, ny))

        if val == 'P' or val == '#':
            return child_values[0]

        if val in operators:
            a, b = max(child_values), min(child_values)
            return operators[val](a, b)

        return 0

    start_x, start_y = 0, 0
    for r in range(N):
        for c in range(M):
            if circuit[r][c] == 'P':
                start_x, start_y = r, c
                break



    ans = dfs(start_x, start_y)
    print(ans)


if __name__ == '__main__':
    main()
