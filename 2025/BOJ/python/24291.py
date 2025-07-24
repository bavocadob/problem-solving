n, k = map(int, input().split())

ans = n
cur = n

while cur > 2:
    gap = (cur - 3) // (k + 2) if cur > 2 else 0

    prev = cur - 1 - gap

    if prev < 2:
        break

    if cur == prev + (prev - 2) // (k + 1) + 1:
        cur = prev
        ans = cur
    else:
        break

print(ans)
