import math

x, y = map(int, input().split())
target = x / y
best_num, best_den = 0, 1
min_diff = float('inf')

for den in range(1, 32768):
    for num in range(max(1, int(target * den) - 1), min(32767, int(target * den) + 2)):
        if math.gcd(num, den) != 1:
            continue

        temp = num / den
        if temp == target:
            continue
        diff = abs(temp - target)
        if diff < min_diff:
            min_diff = diff
            best_num = num
            best_den = den

print(best_num, best_den)
