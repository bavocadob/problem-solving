import sys

input = sys.stdin.readline
N, Q = map(int, input().split())

sets = []
for _ in range(N):
    line = list(map(int, input().split()))
    sets.append(set(line[1:]))

results = []

for _ in range(Q):
    q = list(map(int, input().split()))
    q_type = q[0]

    if q_type == 1:
        a, b = q[1] - 1, q[2] - 1
        if a == b:
            continue

        if len(sets[a]) < len(sets[b]):
            sets[b].update(sets[a])
            sets[a] = sets[b]
            sets[b] = set()
        else:
            sets[a].update(sets[b])
            sets[b] = set()
    elif q_type == 2:
        print(len(sets[q[1] - 1]))
