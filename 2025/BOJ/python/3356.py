def fail(s):
    f = [0] * len(s)

    j = 0

    for i in range(1, len(s)):

        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
            f[i] = j

    return f


N = int(input())

S = input().rstrip()

sf = fail(S)
print(len(S) - sf[-1])