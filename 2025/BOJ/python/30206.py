import sys
from collections import deque

input = sys.stdin.readline
MOD = 1_000_000_007
N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque([1])

ans = 0
dp = [0] * (N + 1)
dp[1] = 1
size = [0] * (N + 1)


while queue:
    while queue:
        cur = queue.popleft()
        size[dp[cur]] += 1

        for next_node in adj[cur]:
            if dp[next_node] == 0:
                dp[next_node] = dp[cur] + 1
                queue.append(next_node)

ans = 1
for i in range(1, N + 1):
    if not size[i]:
        break

    ans = (ans * (size[i] + 1)) % MOD

print(ans - 1)

