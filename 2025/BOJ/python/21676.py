import math

x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())

ans = 0
rr = r * r

sx = max(x1, x3 - r)
ex = min(x2, x3 + r)

for x in range(sx, ex + 1):
    dx_squared = (x - x3) ** 2
    dy_squared = rr - dx_squared

    if dy_squared < 0:
        continue

    dy = math.sqrt(dy_squared)
    min_y = y3 - dy
    max_y = y3 + dy

    sy = max(y1, min_y)
    ey = min(y2, max_y)

    if math.ceil(sy) > math.floor(ey):
        continue

    ans += math.floor(ey) - math.ceil(sy) + 1

print(ans)
