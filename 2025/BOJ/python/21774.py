import sys

input = sys.stdin.readline


def fast_parse(s):
    return int(s[:4] + s[5:7] + s[8:10] + s[11:13] + s[14:16] + s[17:19])


def lower_bound(target, arr):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(target, arr):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def solve(start, end, level):
    ans = 0
    for llv in range(level, 7):
        l = lower_bound(start, levels[llv])
        r = upper_bound(end, levels[llv])
        ans += r - l
    return ans


levels = [[] for _ in range(7)]
N, Q = map(int, input().split())
for _ in range(N):
    t, lv = input().strip().split('#')
    ts = fast_parse(t)
    levels[int(lv)].append(ts)

for i in range(1, 7):
    levels[i].sort()

for _ in range(Q):
    s, e, lv = input().strip().split('#')
    s = fast_parse(s)
    e = fast_parse(e)
    lv = int(lv)
    print(solve(s, e, lv))
