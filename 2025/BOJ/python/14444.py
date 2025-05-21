def manacher(s: list[str]):
    T = '*' + '*'.join(s) + '*'

    n = len(T)
    f = [0] * n
    center = right = 0

    for i in range(n):

        mirror = center * 2 - i

        if right > i:
            f[i] = min(f[mirror], right - i)

        while i + f[i] + 1 < n and i - f[i] - 1 >= 0 and T[i + f[i] + 1] == T[i - f[i] - 1]:
            f[i] += 1

        if i + f[i] > right:
            center = i
            right = i + f[i]

    return max(f)


S = input().rstrip()
print(manacher(S))
