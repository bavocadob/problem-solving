import sys

P1, M1 = 31, 10 ** 9 + 7
P2, M2 = 37, 10 ** 9 + 9

p1m1, p2m1, p1m2, p2m2 = [], [], [], []

input = sys.stdin.readline


def precompute(g, n, m):
    int_g = [[int(c) + 1 for c in row] for row in g]
    h1 = [[0] * (m + 1) for _ in range(n + 1)]
    h2 = [[0] * (m + 1) for _ in range(n + 1)]

    for r in range(n):
        for c in range(m):
            h1[r + 1][c + 1] = (h1[r + 1][c] * P1 + int_g[r][c]) % M1
            h2[r + 1][c + 1] = (h2[r + 1][c] * P1 + int_g[r][c]) % M2

    for c in range(1, m + 1):
        for r in range(1, n + 1):
            h1[r][c] = (h1[r - 1][c] * P2 + h1[r][c]) % M1
            h2[r][c] = (h2[r - 1][c] * P2 + h2[r][c]) % M2

    return h1, h2


def get_hash(h1, h2, r, c, k):
    r1, c1 = r + 1, c + 1
    r2, c2 = r + k, c + k

    t1_2 = (h1[r1 - 1][c2] * p2m1[k]) % M1
    t1_3 = (h1[r2][c1 - 1] * p1m1[k]) % M1
    t1_4 = (h1[r1 - 1][c1 - 1] * p2m1[k]) % M1
    t1_4 = (t1_4 * p1m1[k]) % M1
    val1 = (((h1[r2][c2] - t1_2 + M1) % M1 - t1_3 + M1) % M1 + t1_4) % M1

    t2_2 = (h2[r1 - 1][c2] * p2m2[k]) % M2
    t2_3 = (h2[r2][c1 - 1] * p1m2[k]) % M2
    t2_4 = (h2[r1 - 1][c1 - 1] * p2m2[k]) % M2
    t2_4 = (t2_4 * p1m2[k]) % M2
    val2 = (((h2[r2][c2] - t2_2 + M2) % M2 - t2_3 + M2) % M2 + t2_4) % M2

    return val1, val2


def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    global p1m1, p2m1, p1m2, p2m2
    max_d = max(n, m)
    p1m1, p2m1 = [1] * (max_d + 1), [1] * (max_d + 1)
    p1m2, p2m2 = [1] * (max_d + 1), [1] * (max_d + 1)

    for i in range(1, max_d + 1):
        p1m1[i] = (p1m1[i - 1] * P1) % M1
        p2m1[i] = (p2m1[i - 1] * P2) % M1
        p1m2[i] = (p1m2[i - 1] * P1) % M2
        p2m2[i] = (p2m2[i - 1] * P2) % M2

    h1, h2 = precompute(grid, n, m)
    rot_g = [row[::-1] for row in grid[::-1]]
    # for row in rot_g:
    #     print(row)
    rh1, rh2 = precompute(rot_g, n, m)

    def check(k):
        if k <= 1 or k > min(n, m):
            return False

        # print(k)
        for r in range(n - k + 1):
            for c in range(m - k + 1):
                orig_hash = get_hash(h1, h2, r, c, k)
                rot_r, rot_c = n - r - k, m - c - k
                rot_hash = get_hash(rh1, rh2, rot_r, rot_c, k)
                if orig_hash == rot_hash:
                    return True
        return False

    ans_e, ans_o = 0, 0

    l, r = 1, min(n, m) // 2
    while l <= r:
        mid = (l + r) // 2
        k = mid * 2
        if check(k):
            ans_e = k
            l = mid + 1
        else:
            r = mid - 1

    l, r = 1, (min(n, m) + 1) // 2
    while l <= r:
        mid = (l + r) // 2
        k = mid * 2 - 1

        if k <= 1:
            l = mid + 1
            continue
        if check(k):
            ans_o = k
            l = mid + 1
        else:
            r = mid - 1

    ans = max(ans_e, ans_o)

    if ans > 1:
        print(ans)
    else:
        print(-1)


if __name__ == '__main__':
    main()
