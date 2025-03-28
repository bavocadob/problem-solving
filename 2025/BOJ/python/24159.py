from collections import Counter


def mod_pow(base, exp, mod):
    rst = 1
    while exp:
        if exp % 2:
            rst = (rst * base) % mod
        base = (base * base) % mod
        exp //= 2
    return rst


p = int(input())
n = int(input())
a = [mod_pow(i, n, p) for i in range(p)]

count_a = Counter(a)

count_c = Counter()
for i in range(p):
    count_c[(a[i] + a[i]) % p] += 1

    for j in range(i + 1, p):
        count_c[(a[i] + a[j]) % p] += 2

print(sum(count_a[z] * count_c[z] for z in range(p)))
