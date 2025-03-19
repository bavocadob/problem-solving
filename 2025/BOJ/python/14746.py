N, M = map(int, input().split())
y1, y2 = map(int, input().split())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

P.sort()
Q.sort()

l = 0
r = 0

max_gap = int(1e9)
cnt = 0

while l < N and r < M:

    temp = abs(P[l] - Q[r])
    if max_gap > temp:
        max_gap = temp
        cnt = 1
    elif max_gap == temp:
        cnt += 1

    if P[l] >= Q[r]:
        r += 1
    else:
        l += 1

print(max_gap + abs(y1 - y2), cnt)
