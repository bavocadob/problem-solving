import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

A, B, C = map(int, input().split())

adj = [list() for _ in range(N + 1)]
for _ in range(M):
    n1, n2, cost = map(int, input().split())
    adj[n1].append((n2, cost))
    adj[n2].append((n1, cost))


def bfs(start, dist):
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v, _ in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)


distB = [-1] * (N + 1)
distC = [-1] * (N + 1)
bfs(B, distB)
bfs(C, distC)

max_len = distB[C]

next_ptr = [-1] * (N + 1)

for u in range(1, N + 1):
    if distB[u] == -1 or distB[u] >= max_len:
        continue

    best_v = -1
    best_deg = -1
    for v, _ in adj[u]:
        if distB[v] == distB[u] + 1 and distB[v] + distC[v] == max_len:
            deg = len(adj[v])
            if deg > best_deg or (deg == best_deg and v > best_v):
                best_deg, best_v = deg, v

    next_ptr[u] = best_v

route = set()
u = B
while u != -1:
    route.add(u)
    if u == C:
        break
    u = next_ptr[u]

INF = float('inf')

distances = [INF] * (N + 1)
distances[A] = 0

queue = [(0, A)]

ans = -1
ans_dist = INF

while queue:
    dist, node = heapq.heappop(queue)
    if distances[node] != dist:
        continue

    if dist > ans_dist:
        break
    if node in route:
        if ans_dist > dist:
            ans = node
            ans_dist = dist
        elif ans_dist == dist:
            ans = min(node, ans)

    for next_node, cost in adj[node]:
        next_dist = dist + cost
        if distances[next_node] > next_dist:
            distances[next_node] = next_dist
            heapq.heappush(queue, (next_dist, next_node))

print(ans)
