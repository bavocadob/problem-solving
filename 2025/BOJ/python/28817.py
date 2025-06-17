def fail(s):
    n = len(s)
    f = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
        f[i] = j
    return f


def main():
    s = input().rstrip()
    L = len(s)

    if L < 3:
        print(0)
        return

    s_rev = s[::-1]
    f_s = fail(s)
    f_rev = fail(s_rev)

    a = 0
    for i in range(1, (L - 1) // 2 + 1):
        k = 2 * i
        d = k - f_s[k - 1]
        if i % d == 0:
            a += 1

    b = 0
    for i in range(1, (L - 1) // 2 + 1):
        k = 2 * i
        d_rev = k - f_rev[k - 1]
        if i % d_rev == 0:
            b += 1

    c = 0
    border_len = f_s[L - 1]
    while border_len * 2 > L:
        c += 1
        border_len = f_s[border_len - 1]

    d = 0
    if L % 3 == 0:
        i = L // 3
        if s[:i] == s[i:2 * i] and s[:i] == s[2 * i:]:
            d = 1

    total = (L - 1) * (L - 2) // 2
    ex = a + b + c - 2 * d

    print(total - ex)


if __name__ == '__main__':
    main()
