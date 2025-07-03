import sys
from math import lcm


def main():
    input = sys.stdin.readline

    N, L = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    bb = []
    lcm_val = 1
    for i in range(N):
        if B[i]:
            lcm_val = lcm(lcm_val, A[i])
            if lcm_val > L:
                print(-1)
                return
        else:
            bb.append(A[i])

    if lcm_val > L:
        print(-1)
        return

    for b in bb:
        if lcm_val % b == 0:
            print(-1)
            return

    print(lcm_val)


if __name__ == '__main__':
    main()
