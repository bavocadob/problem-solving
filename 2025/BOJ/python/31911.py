import sys
from collections import defaultdict

input = sys.stdin.readline

CHAR_TO_INDEX = {
    '-': 0,
    '[': 1,
    ']': 2,
    **{chr(i): i - ord('a') + 3 for i in range(ord('a'), ord('z') + 1)}
}

INDEX_TO_CHAR = {v: k for k, v in CHAR_TO_INDEX.items()}


def learn(s, graph, to_idx):
    for i in range(len(s) - 1):
        a, b = to_idx[s[i]], to_idx[s[i + 1]]
        graph[a][b] += 1


def get_path(graph, to_chr):
    base, cycle = '[', ''
    visited = defaultdict(int)
    cur = CHAR_TO_INDEX['[']

    while True:
        nxt_dict = graph[cur]
        max_cnt, nxt = 0, None

        for i, cnt in nxt_dict.items():
            if cnt > max_cnt or (cnt == max_cnt and (nxt is None or i < nxt)):
                max_cnt, nxt = cnt, i

        if max_cnt == 0:
            break

        visited[nxt] += 1
        ch = to_chr[nxt]

        if visited[nxt] == 1:
            base += ch
        elif visited[nxt] == 2:
            cycle += ch
        else:
            break

        cur = nxt

    return base[:len(base) - len(cycle)], cycle


def solve(base, cycle, start, length):
    res = ''
    clen = len(cycle)

    if start < len(base):
        res += base[start:start + length]

    remain = length - len(res)
    if remain > 0 and clen > 0:
        s = (start - len(base)) % clen if start >= len(base) else 0
        times = (remain // clen) + 1
        res += (cycle * (times + 1))[s:s + remain]

    res += '.' * (length - len(res))
    return res


def main():
    n, m, k = map(int, input().split())
    graph = [defaultdict(int) for _ in range(29)]

    for _ in range(n):
        learn(input().strip(), graph, CHAR_TO_INDEX)

    base, cycle = get_path(graph, INDEX_TO_CHAR)
    print(solve(base, cycle, m - 1, k))


if __name__ == "__main__":
    main()
