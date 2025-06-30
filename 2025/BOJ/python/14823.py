import sys
from collections import deque

input = sys.stdin.readline


def get_prev(g):
    L = len(g)
    counts = [0] * (L + 1)
    sum_of_counts = 0

    for i in range(L):
        count = int(g[i])
        counts[i + 1] = count
        sum_of_counts += count

    if sum_of_counts > L:
        return set()

    counts[0] = L - sum_of_counts

    prev = set()

    def backtrack(path, current_counts):
        if len(path) == L:
            prev.add("".join(path))
            return

        for digit in range(L + 1):
            if current_counts[digit] > 0:
                current_counts[digit] -= 1

                path.append(str(digit))
                backtrack(path, current_counts)
                path.pop()

                current_counts[digit] += 1

    backtrack([], counts)
    return prev


def solve(g):
    rst = {g}
    queue = deque([g])

    while queue:
        current = queue.popleft()

        prev = get_prev(current)

        for p in prev:
            if p in rst:
                continue
            rst.add(p)
            queue.append(p)

    return len(rst)


def main():
    T = int(input())
    for i in range(1, T + 1):
        G = input().strip()
        result = solve(G)
        print(f"Case #{i}: {result}")


if __name__ == "__main__":
    main()
