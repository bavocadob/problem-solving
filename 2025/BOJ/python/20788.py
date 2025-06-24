import sys

MOD = 1_000_000_007
input = sys.stdin.readline


def fail(a):
    n = len(a)
    f = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and a[i] != a[j]:
            j = f[j - 1]
        if a[i] == a[j]:
            j += 1
            f[i] = j
    return f


def kmp(text, pattern, f):
    n, m = len(text), len(pattern)

    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = f[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                return True
            else:
                j += 1
    return False


def main():
    try:
        for _ in range(200001):

            N = int(input())
            A = list(map(int, input().split()))

            rev_A = A[::-1]

            if A == rev_A:
                f = fail(A)
                L = f[-1] if N > 0 else 0
                k = N - L
                if N % k == 0:
                    print(k % MOD)
                else:
                    print(N % MOD)
                continue

            f = fail(A)
            L_A = f[-1] if N > 0 else 0
            k_A = N - L_A
            if N % k_A != 0:
                k_A = N

            rev_f = fail(rev_A)
            L_rev_A = rev_f[-1] if N > 0 else 0
            k_rev_A = N - L_rev_A
            if N % k_rev_A != 0:
                k_rev_A = N

            is_cycle = kmp(A + A, rev_A, rev_f)

            if is_cycle:
                print(k_A % MOD)
            else:
                print((k_A + k_rev_A) % MOD)
    except:
        return


if __name__ == '__main__':
    main()
