from math import gcd


def failure(s):
    f = [0] * len(s)

    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]

        if s[i] == s[j]:
            j += 1
            f[i] = j

    return f


def kmp(s, f):
    m = len(f)
    j = 0
    rst = 0

    for i in range(len(s)):
        while j > 0 and s[i] != target[j]:
            j = f[j - 1]

        if s[i] == target[j]:
            if j == m - 1:
                rst += 1
                j = f[j]
            else:
                j += 1

    return rst


N = int(input())

target = ''.join(input().split())
roulette = ''.join(input().split())
roulette += roulette[:len(roulette) - 1]

cnt = kmp(roulette, failure(target))

div = gcd(cnt, N)

print(f'{cnt // div}/{N // div}')
