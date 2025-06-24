import sys

input = sys.stdin.readline

MAX = 1000001

n = int(input())
deposits = list(map(int, input().split()))
counts = [0] * MAX
for d in deposits:
    counts[d] += 1

m = int(input())
requests = list(map(int, input().split()))
request_cnt = [0] * MAX
for r in requests:
    request_cnt[r] += 1

multiples_count = [0] * MAX
for i in range(1, MAX):
    for j in range(i, MAX, i):
        multiples_count[i] += counts[j]

ans = 0
for i in range(1, MAX):
    if request_cnt[i] > 0:
        ans += multiples_count[i] * request_cnt[i]

print(ans)
