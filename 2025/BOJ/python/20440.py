import sys

input = sys.stdin.readline

N = int(input())

time_set = set()

queries = []
for _ in range(N):
    s, e = map(int, input().split())
    queries.append((s, e))
    time_set.add(s)
    time_set.add(e)

time_list = sorted(time_set)
del time_set

time_map = dict()

for i in range(len(time_list)):
    time_map[time_list[i]] = i

prefix_sum = [0] * (len(time_list))

for s, e in queries:
    s_pos = time_map[s]
    e_pos = time_map[e]
    prefix_sum[s_pos] += 1
    prefix_sum[e_pos] -= 1

for i in range(1, len(time_list)):
    prefix_sum[i] += prefix_sum[i - 1]

l = r = size = 0

for i in range(len(prefix_sum) - 1):
    if prefix_sum[i] > size:
        size = prefix_sum[i]
        l = time_list[i]
        r = time_list[i + 1]
    elif prefix_sum[i] == size and prefix_sum[i - 1] == size:
        r = time_list[i + 1]



print(size)
print(l, r)
