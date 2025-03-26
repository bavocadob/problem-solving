import sys
from collections import defaultdict

input = sys.stdin.readline


def solve():
    word = input().strip()
    k = int(input())

    if k == 1:
        print('1 1')
        return

    alpha = defaultdict(list)

    for i in range(len(word)):
        alpha[word[i]].append(i)

    min_ans = int(1e9)
    max_ans = 0
    for pos_list in alpha.values():
        if len(pos_list) < k:
            continue

        for i in range(k - 1, len(pos_list)):
            temp = pos_list[i] - pos_list[i - k + 1] + 1
            min_ans = min(min_ans, temp)
            max_ans = max(max_ans, temp)

    if min_ans == int(1e9):
        print(-1)
    else:
        print(min_ans, max_ans)


T = int(input())

for _ in range(T):
    solve()
