import sys
from collections import defaultdict

input = sys.stdin.readline


def get_subset(items, subset_size):
    num_items = len(items)
    subset_size[0][(0, 0)] = 1

    for bitmask in range(1, 1 << num_items):
        x, y = 0, 0
        size = 0
        for i in range(num_items):
            if (bitmask >> i) & 1:
                item_x, item_y = items[i]
                x += item_x
                y += item_y
                size += 1

        subset_size[size][(x, y)] += 1


def solve(k, left, right, xg, yg):
    ans = 0

    max_l = len(left) - 1
    max_r = len(right) - 1
    for i in range(k + 1):
        j = k - i

        if not (0 <= i <= max_l and 0 <= j <= max_r):
            continue

        map_i = left[i]
        map_j = right[j]

        if not map_i or not map_j:
            continue

        if len(map_i) > len(map_j):
            for (xj, yj), count_j in map_j.items():
                xi_needed = xg - xj
                yi_needed = yg - yj
                if (xi_needed, yi_needed) in map_i:
                    ans += count_j * map_i[(xi_needed, yi_needed)]
        else:
            for (xi, yi), count_i in map_i.items():
                xj_needed = xg - xi
                yj_needed = yg - yi
                if (xj_needed, yj_needed) in map_j:
                    ans += count_i * map_j[(xj_needed, yj_needed)]
    return ans


def main():
    N = int(input())
    xg, yg = map(int, input().split())

    l_size = N // 2 + N % 2
    r_size = N // 2

    left = [defaultdict(int) for _ in range(l_size + 1)]
    right = [defaultdict(int) for _ in range(r_size + 1)]

    items_A = []
    for _ in range(l_size):
        items_A.append(tuple(map(int, input().split())))

    items_B = []
    for _ in range(r_size):
        items_B.append(tuple(map(int, input().split())))

    get_subset(items_A, left)
    get_subset(items_B, right)

    for i in range(1, N + 1):
        print(solve(i, left, right, xg, yg))


if __name__ == '__main__':
    main()
