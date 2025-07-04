# from math import pow

MOD = 1_000_000_007


def main():
    N = int(input())

    base = pow(2, N, MOD)
    if N % 3 != 2:
        print(base)
        return

    k = N // 3
    temp = pow(2, k + 1, MOD)
    print((base - temp + MOD) % MOD)


if __name__ == '__main__':
    main()
