import sys

input = sys.stdin.readline


def find(p, node):
    if p[node] == node:
        return node

    parent = find(p, p[node])
    p[node] = parent
    return parent


def union(p, x, y):
    px = find(p, x)
    py = find(p, y)

    if px == py:
        return

    if px > py:
        py, px = px, py

    power[px] += size[px] * size[py] + power[py]

    size[px] += size[py]
    p[py] = px


N, Q = map(int, input().split())

power = [0] * (N + 1)
size = [0] * (N + 1)
parents = [i for i in range(N + 1)]
nadori = list(map(int, input().split()))

for i in range(N):
    size[i + 1] = nadori[i]

for _ in range(Q):
    a, b = map(int, input().split())
    pa, pb = find(parents, a), find(parents, b)

    if pa == pb:
        print(power[pa])
    else:
        union(parents, pa, pb)
        print(power[find(parents, pa)])
