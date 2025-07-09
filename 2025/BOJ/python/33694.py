import sys

input = sys.stdin.readline


def calc(a, b, c, t, x):
    days_to_reach_c = (c + a - 1) // a
    peak_day = t + days_to_reach_c
    peak_size = a * days_to_reach_c

    if x > peak_size:
        return None

    days_to_reach_x = (x + a - 1) // a
    start_day = t + days_to_reach_x

    days_to_decrease = (peak_size - x) // b
    end_day = peak_day + days_to_decrease

    return start_day, end_day


N, X = map(int, input().split())

prefix = []
for _ in range(N):
    A, B, C, T = map(int, input().split())

    interval = calc(A, B, C, T, X)
    if interval:
        start, end = interval
        prefix.append((start, 1))
        prefix.append((end + 1, -1))

prefix.sort()

ans = 0
cur_slimes = 0
cur_day = 0

if prefix:
    cur_day = prefix[0][0]

for i in range(len(prefix)):
    day, cnt = prefix[i]
    # print(day, cnt, cur_slimes)
    if day > cur_day:
        if cur_slimes >= 3:
            ans += (day - cur_day)

    cur_slimes += cnt
    cur_day = day

print(ans)
