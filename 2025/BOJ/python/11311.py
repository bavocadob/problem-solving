import sys

input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(a, b, d):
    cd = gcd(a, b)

    if d % cd == 0:
        return 'Yes'

    return 'No'


def main():
    T = int(input())

    for _ in range(T):
        a, b, d = map(int, input().split())

        ans = solve(a, b, d)
        print(ans)


if __name__ == '__main__':
    main()
