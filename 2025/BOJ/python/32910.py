import sys


def check(seq, length):
    if length == 0:
        return 0

    k = length

    factors = []
    d = 2
    temp = length
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)

    for p in factors:
        cand = k // p
        is_periodic = True
        for i in range(length):
            if seq[i] != seq[i % cand]:
                is_periodic = False
                break

        while is_periodic:
            k = cand
            if k % p != 0:
                break

            cand = k // p
            is_periodic = True
            for i in range(length):
                if seq[i] != seq[i % cand]:
                    is_periodic = False
                    break
    return k


input = sys.stdin.readline

n, m = map(int, input().split())
a = input().split()
b = input().split()

len_a = check(a, n)
prim_a = "".join(a[:len_a])

len_b = check(b, m)
prim_b = "".join(b[:len_b])

if len_a == len_b and prim_b in prim_a + prim_a:
    print("YES")
else:
    print("NO")
