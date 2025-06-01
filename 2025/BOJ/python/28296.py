import sys
from collections import defaultdict

input = sys.stdin.readline


def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]


def union(x, y, cost, parent, size, com_d, ans):
    px = find(parent, x)
    py = find(parent, y)

    if px == py:
        return

    if size[px] < size[py]:
        px, py = py, px

    parent[py] = px
    size[px] += size[py]
    if len(com_d[px]) < len(com_d[py]):
        com_d[px], com_d[py] = com_d[py], com_d[px]

    for i, count in com_d[py].items():
        p_count = com_d[px][i]

        if p_count > 0:
            ans[i] += p_count * count * cost

        com_d[px][i] = p_count + count

    com_d[py].clear()


def main():
    n, k, m = map(int, input().split())
    companies = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    parent = list(range(n + 1))
    size = [1] * (n + 1)
    company_dict = [defaultdict(int) for _ in range(n + 1)]
    ans = [0] * (k + 1)

    for i in range(n):
        company_dict[i + 1][companies[i]] = 1

    edges.sort(reverse=True)

    for cost, u, v in edges:
        union(u, v, cost, parent, size, company_dict, ans)

    for i in range(1, k + 1):
        print(ans[i])


if __name__ == "__main__":
    main()
