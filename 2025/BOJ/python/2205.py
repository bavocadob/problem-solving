def great_power_of_two(n):
    def next_power_of_two(n):
        if n <= 0:
            return 1

        n -= 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        n |= n >> 32
        return n + 1

    power = next_power_of_two(n)

    return power if power > n else power << 1


N = int(input())

ans = [0] * (N + 1)

cur = N

while cur >= 1:
    target = great_power_of_two(cur)
    nxt = target - cur

    for i in range(nxt, cur + 1):
        ans[i] = target - i

    cur = nxt - 1

for i in range(1, N + 1):
    print(ans[i])
