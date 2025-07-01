def solve():
    n = int(input())

    l = 1
    r = 10 ** 6
    i = 0

    while l <= r:
        mid = (l + r) // 2
        length = 13 * mid * (mid + 1)

        if n <= length:
            i = mid
            r = mid - 1
        else:
            l = mid + 1

    prev_size = 13 * (i - 1) * i

    nth = n - prev_size

    idx = (nth - 1) // i
    return chr(ord('A') + idx)


t = int(input())
for i in range(1, t + 1):
    rst = solve()
    print(f'Case #{i}: {rst}')
