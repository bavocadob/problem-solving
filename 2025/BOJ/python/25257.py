d, s, e = map(int, input().split())
R = d - s - e

if R >= s:
    p = (d - s) / d * (s / R)
else:
    p = (s + e) / d

print(p)
