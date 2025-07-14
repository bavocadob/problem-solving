import sys

input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())

    mtm = (N + 1) * (2 ** M)

    if K <= mtm:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
