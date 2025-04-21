def find(level, width, length):
    if level <= 2:
        return 1
    left = fib[level - 2]
    right = fib[level - 1]

    if left <= width < right:
        return level

    if width >= right:
        width -= right

    return find(level - 1, length, width)


a, b = map(int, input().split())
x, y = map(int, input().split())
fib = [1, 1]
while fib[-1] < max(a, b):
    fib.append(fib[-1] + fib[-2])

if a < b:
    a, b = b, a
    x, y = y, x

n = 0
for i in range(2, len(fib)):
    if fib[i - 1] == b and fib[i] == a:
        n = i
        break

print(find(n, x, y))
