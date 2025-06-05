import sys

input = sys.stdin.readline
BASE = 71
MOD = 1_000_000_007


def atoi(c):
    if c == 'o':
        return 1
    return 2


def fail(arr):
    n = len(arr)
    f = [0] * n

    j = 0

    for i in range(1, n):
        while j > 0 and arr[i] != arr[j]:
            j = f[j - 1]

        if arr[i] == arr[j]:
            j += 1
            f[i] = j

    return f


def kmp(pattern, arr, f):
    j = 0
    cnt = 0

    for i in range(len(arr)):
        while j > 0 and pattern[j] != arr[i]:
            j = f[j - 1]

        if pattern[j] == arr[i]:
            j += 1
            if j == len(pattern):
                cnt += 1
                j = f[j - 1]
    return cnt


def make_hash_val(arr, length):
    rst = 0

    for i in range(length):
        rst = ((rst * BASE) + arr[i]) % MOD

    return rst


def make_int_arr(arr, n, m):
    for i in range(n):
        for j in range(m):
            arr[i][j] = atoi(arr[i][j])


def main():
    hp, wp, hm, wm = map(int, input().split())

    patterns = [list(input()) for _ in range(hp)]
    masterpiece = [list(input()) for _ in range(hm)]

    make_int_arr(patterns, hp, wp)
    make_int_arr(masterpiece, hm, wm)

    pattern_hash = []

    for i in range(hp):
        pattern_hash.append(make_hash_val(patterns[i], wp))

    f = fail(pattern_hash)

    masterpiece_hash = [[0] * (wm - wp + 1) for _ in range(hm)]
    POWER_BASE = pow(BASE, wp - 1, MOD)
    for i in range(hm):
        row = masterpiece[i]
        cur = make_hash_val(row, wp)
        masterpiece_hash[i][0] = cur

        for j in range(1, wm - wp + 1):
            prev = POWER_BASE * row[j - 1]
            cur = (cur - prev + MOD) % MOD
            cur = (cur * BASE + row[j + wp - 1]) % MOD
            masterpiece_hash[i][j] = cur

    masterpiece_hash = list(map(list, zip(*masterpiece_hash)))

    ans = 0
    for row in masterpiece_hash:
        ans += kmp(pattern_hash, row, f)

    print(ans)


if __name__ == '__main__':
    main()
