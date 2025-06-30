from collections import defaultdict

N = int(input())

cities = defaultdict(int)

A = list(map(int, input().split()))

for a in A:
    cities[a] += 1

rst = [0] * (N + 1)

cnt = defaultdict(int)
for city, size in cities.items():
    cnt[size] += 1

for size, c in cnt.items():
    for i in range(1, N + 1):
        if i > size:
            break
        rst[i] += i * (size // i) * c

print(*rst[1:])
