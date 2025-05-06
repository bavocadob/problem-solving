def solve(s1, s2):
    pre1, suf1 = s1.split('*')
    pre2, suf2 = s2.split('*')

    min_len = max(len(pre1) + len(suf1), len(pre2) + len(suf2))
    max_extend = len(pre1) + len(suf1) + len(pre2) + len(suf2)

    for L in range(min_len, min_len + max_extend + 1):
        T = ['?'] * L
        ok = True

        for i, ch in enumerate(pre1):
            if T[i] in ('?', ch):
                T[i] = ch
            else:
                ok = False
                break
        for i, ch in enumerate(suf1):
            pos = L - len(suf1) + i
            if T[pos] in ('?', ch):
                T[pos] = ch
            else:
                ok = False
                break

        # print(T, 's1 적용후')
        if not ok:
            continue

        for i, ch in enumerate(pre2):
            if T[i] in ('?', ch):
                T[i] = ch
            else:
                ok = False
                break
        for i, ch in enumerate(suf2):
            pos = L - len(suf2) + i
            if T[pos] in ('?', ch):
                T[pos] = ch
            else:
                ok = False
                break
        # print(T, 's2 적용후')
        if not ok:
            continue

        return ''.join(T)

    return '-1'


a = input().rstrip()
b = input().rstrip()
print(solve(a, b))

