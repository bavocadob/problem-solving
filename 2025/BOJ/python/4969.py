import sys

input = sys.stdin.readline


def main():
    MAX_NUM = 300000
    is_ms_prime = [False] * (MAX_NUM + 1)

    for i in range(2, MAX_NUM + 1):
        if i % 7 == 1 or i % 7 == 6:
            is_ms_prime[i] = True

    for i in range(2, MAX_NUM + 1):
        if not is_ms_prime[i]:
            continue
        for j in range(i * 2, MAX_NUM + 1, i):
            if j % 7 == 1 or j % 7 == 6:
                is_ms_prime[j] = False

    while True:
        n = int(input())

        if n == 1:
            break

        rst = []

        for d in range(2, n + 1):
            if n % d == 0:
                if is_ms_prime[d]:
                    rst.append(str(d))

        print(f'{n}: {" ".join(rst)}')


if __name__ == '__main__':
    main()
