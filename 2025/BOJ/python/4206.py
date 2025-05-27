import sys

input = sys.stdin.readline


def get_pattern(s):
    f = [0] * len(s)

    j = 0

    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]

        if s[i] == s[j]:
            j += 1
            f[i] = j

    return f


def kmp(a, b, f):
    j = 0

    rst = 0
    for i in range(len(a)):
        while j > 0 and b[j] != a[i]:
            j = f[j - 1]
        if b[j] == a[i]:
            j += 1
            if j == len(f):
                rst += 1
                j = f[j - 1]

    return rst


def set_head(head, length):
    if length == 1:
        head[0] = [1]
        return

    if len(head[0]) == length:
        return

    temp = head[0][:]
    head[0] = head[1][:]

    for i in range(len(temp)):
        if len(head[1]) == length:
            return

        head[1].append(temp[i])


def set_tail(tail, length):
    if len(tail[0]) == length:
        tail[0], tail[1] = tail[1], tail[0]
        return

    temp = tail[0][:]
    tail[0] = tail[1][:]

    tail[1] = tail[1][len(tail[1]) - min(len(tail[1]), (length - len(temp))):] + temp


def solve(n, p):
    if n == 0:
        return int(p == [0])

    if n == 1:
        return int(p == [1])

    f = get_pattern(p)

    size = len(p) - 1

    dp = [0] * 2

    if size == 0:
        if p == [0]:
            dp[0] = 1
        else:
            dp[1] = 1

        for i in range(2, n + 1):
            dp.append(dp[-1] + dp[-2])
        return dp[n]

    head = [[0], [1]]
    tail = [[0], [1]]

    for i in range(2, n + 1):
        concat = tail[1] + head[0]
        cur = sum(dp) + kmp(concat, p, f)

        # print(f'i : {i},    tail {tail}      head : {head}')
        # print(''.join(map(str, head[1])))
        kmp(concat, p, f)
        dp[0], dp[1] = dp[1], cur

        set_head(head, size)
        set_tail(tail, size)

    return cur


def main():
    t = 1

    while True:
        try:
            n = int(input())
            p = list(map(int, input().rstrip()))
            ans = solve(n, p)

            print(f'Case {t}: {ans}')
            t += 1
        except:
            break


if __name__ == '__main__':
    main()
