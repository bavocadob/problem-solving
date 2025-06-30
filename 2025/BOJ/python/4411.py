import math
import sys

input = sys.stdin.readline


def count_levels(n):
    if n == 0:
        return 0

    s = bin(n)[2:]
    length = len(s)
    rst = 0
    prefix_one = 0

    for i in range(length):
        remain = length - 1 - i

        if s[i] == '1':
            for j in range(remain + 1):
                if (prefix_one + j) > 0 and (prefix_one + j) % 3 == 0:
                    rst += math.comb(remain, j)
            prefix_one += 1

    if prefix_one > 0 and prefix_one % 3 == 0:
        rst += 1

    return rst


def main():
    while True:
        try:
            N = int(input())
            level = count_levels(N)

            print(f'Day {N}: Level = {level}')
        except:
            break


if __name__ == "__main__":
    main()
