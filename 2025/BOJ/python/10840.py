P1, P2, MOD1, MOD2 = 31, 37, 1_000_000_007, 1_000_000_009


def atoi(char):
    return ord(char) - ord('a')


def init_hash(freq, table_1, table_2):
    h1, h2 = 0, 0

    for i in range(26):
        h1 += (table_1[i] * freq[i]) % MOD1
        h1 %= MOD1

        h2 += (table_2[i] * freq[i]) % MOD2
        h2 %= MOD2

    return h1, h2


def solve(a, b, t1, t2, length):
    if length == 0:
        return True

    freq = [0] * 26

    h_set = set()
    for i in range(length):
        freq[a[i]] += 1

    h1, h2 = init_hash(freq, t1, t2)
    h_set.add((h1, h2))

    for i in range(len(a) - length):
        out_h1 = t1[a[i]]
        in_h1 = t1[a[i + length]]

        h1 = h1 - out_h1 + in_h1
        h1 = (h1 + MOD1) % MOD1

        out_h2 = t2[a[i]]
        in_h2 = t2[a[i + length]]

        h2 = h2 - out_h2 + in_h2
        h2 = (h2 + MOD2) % MOD2

        h_set.add((h1, h2))

    freq = [0] * 26

    for i in range(length):
        freq[b[i]] += 1

    h1, h2 = init_hash(freq, t1, t2)
    if (h1, h2) in h_set:
        return True

    for i in range(len(b) - length):
        out_h1 = t1[b[i]]
        in_h1 = t1[b[i + length]]

        h1 = h1 - out_h1 + in_h1
        h1 = (h1 + MOD1) % MOD1

        out_h2 = t2[b[i]]
        in_h2 = t2[b[i + length]]

        h2 = h2 - out_h2 + in_h2
        h2 = (h2 + MOD2) % MOD2

        if (h1, h2) in h_set:
            return True

    return False


def main():
    sa = input().rstrip()
    sb = input().rstrip()

    if len(sa) < len(sb):
        sa, sb = sb, sa

    a = [0] * len(sa)
    b = [0] * len(sb)

    for i in range(len(sa)):
        a[i] = atoi(sa[i])

    for i in range(len(sb)):
        b[i] = atoi(sb[i])

    t1 = [1]
    t2 = [1]
    for i in range(25):
        temp = (t1[-1] * P1) % MOD1
        t1.append(temp)

        temp = (t2[-1] * P2) % MOD2
        t2.append(temp)

    for length in range(len(sb), -1, -1):
        if solve(a, b, t1, t2, length):
            print(length)
            break



if __name__ == '__main__':
    main()
