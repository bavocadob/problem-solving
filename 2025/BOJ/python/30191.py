def solve(n, word):
    idx = n - 1

    rst = []
    S_count = 0
    U_count = 0

    length = 0

    while idx >= 0:
        if word[idx] == 'S' and S_count:
            idx -= 1
            S_count -= 1
            rst.append('N')
            length += 1
            continue

        if word[idx] == 'U' and U_count:
            idx -= 1
            U_count -= 1
            rst.append('N')
            length += 1
            continue

        temp = word[idx - 1:idx + 1]
        if temp == 'SU':
            rst.append('SNN')
            length += 3
            idx -= 2
        elif temp == 'US':
            rst.append('UNN')
            length += 3
            idx -= 2
        elif temp == 'SS':
            rst.append('UN')
            length += 2
            idx -= 1
            U_count += 1
        elif temp == 'UU':
            rst.append('SN')
            length += 2
            idx -= 1
            S_count += 1

    print(length)
    print(''.join(rst))


N = int(input())

a = input().strip()
solve(N, a)
