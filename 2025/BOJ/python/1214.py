import math

D, P, Q = map(int, input().split())

g = math.gcd(P, Q)
P //= g
Q //= g
D = (D + g - 1) // g

if P < Q:
    P, Q = Q, P

ans = float('inf')
max_i = min(Q, (D + P - 1) // P)

for i in range(max_i + 1):
    total = i * P
    if total >= D:
        temp = total
    else:
        rem = D - total
        y = (rem + Q - 1) // Q
        temp = total + y * Q
    # print(temp)
    ans = min(ans, temp)

print(ans * g)
