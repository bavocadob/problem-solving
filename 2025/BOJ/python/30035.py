import math
import sys
from collections import defaultdict

input = sys.stdin.readline


def solve(n, t):
    remain = n

    tiers = defaultdict(list)
    rank_start = 1

    for _ in range(t):
        tier, k = input().split()
        if remain <= 0:
            continue

        if k[-1] != '%':
            k = int(k)
        else:
            percent = int(k[:len(k) - 1])
            k = (remain * percent) // 100

        remain -= k
        tier_size = math.ceil(k / 4)
        for i in range(4):
            if k == 0:
                break

            part_size = min(k, tier_size)
            k -= part_size

            tiers[tier].append((rank_start, min(n, rank_start + part_size - 1)))
            rank_start = min(n + 1, rank_start + part_size)

    target_tier = input().strip()
    if rank_start != n + 1:
        print('Invalid System')
        return

    left = right = -1
    if target_tier[-1].isdigit():
        target_tier, target_grade = target_tier[:len(target_tier) - 1], int(target_tier[-1])

        if len(tiers[target_tier]) < target_grade:
            print('Liar')
            return

        left, right = tiers[target_tier][target_grade - 1]
    else:
        if len(tiers[target_tier]) <= 0:
            print('Liar')
            return
        else:
            left, right = tiers[target_tier][0][0], tiers[target_tier][-1][-1]

    print(left, right)


N, T = map(int, input().split())

solve(N, T)
