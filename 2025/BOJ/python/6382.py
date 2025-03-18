import sys
from collections import deque

input = sys.stdin.readline


def bfs(s, e, a):
    queue = deque([s])
    visited = set()
    visited.add(s)

    while queue:
        current = queue.popleft()

        if current == e:
            return True

        for neighbor in a.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


T = 0
while True:
    n = int(input().strip())
    if n == 0:
        break

    T += 1
    data = list(map(int, input().split()))
    start = tuple(data[:n])
    end = tuple(data[n:])

    adj = {}

    while True:
        line = list(map(int, input().split()))
        if line[0] == -1:
            break

        point1 = tuple(line[:n])
        point2 = tuple(line[n:])

        if point1 not in adj:
            adj[point1] = []
        if point2 not in adj:
            adj[point2] = []

        adj[point1].append(point2)
        adj[point2].append(point1)

    if bfs(start, end, adj):
        print(f"Maze #{T} can be travelled")
    else:
        print(f"Maze #{T} cannot be travelled")
