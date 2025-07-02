import sys
import math


input = sys.stdin.readline
def solve(n):
    if n < 3:
        return 'No such base'

    if n == 3:
        return 4

    k = n - 3

    b = float('inf')

    lim = int(math.sqrt(k))
    for i in range(1, lim + 1):
        if k % i == 0:

            div1 = i
            div2 = k // i

            if div1 > 3:
                b = min(b, div1)
            if div2 > 3:
                b = min(b, div2)

    if b == float('inf'):
        if k > 3:
            return k
        else:
            return 'No such base'
    else:
        return b


def main():
    while True:
        N = int(input())
        if N == 0:
            break

        print(solve(N))


if __name__ == '__main__':
    main()
