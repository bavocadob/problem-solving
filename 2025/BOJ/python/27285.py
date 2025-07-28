import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    l_to_r = [[0] * M for _ in range(N)]
    r_to_l = [[0] * M for _ in range(N)]
    u_to_d = [[0] * M for _ in range(N)]
    d_to_u = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):

            if j > 0:
                l_to_r[i][j] = l_to_r[i][j - 1]
                r_to_l[i][M - 1 - j] = r_to_l[i][M - j]

            l_to_r[i][j] = max(l_to_r[i][j], 0) + board[i][j]
            r_to_l[i][M - 1 - j] = max(r_to_l[i][M - 1 - j], 0) + board[i][M - 1 - j]

    for j in range(M):
        for i in range(N):
            if i > 0:
                u_to_d[i][j] = u_to_d[i - 1][j]
                d_to_u[N - 1 - i][j] = d_to_u[N - i][j]

            u_to_d[i][j] = max(u_to_d[i][j], 0) + board[i][j]
            d_to_u[N - 1 - i][j] = max(d_to_u[N - 1 - i][j], 0) + board[N - 1 - i][j]

    ans = -float('inf')

    for i in range(N):
        for j in range(M):
            h = max(l_to_r[i][j], r_to_l[i][j])
            v = max(u_to_d[i][j], d_to_u[i][j])
            # print(f'i : {i}, j : {j} , {h}, {v}, {h + v - board[i][j]}')
            ans = max(ans, h + v - board[i][j])

    print(ans)


if __name__ == '__main__':
    main()
