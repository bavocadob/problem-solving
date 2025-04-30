import sys

input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def _print(num: int, den: int):
    left = num // den
    rem = num % den

    if rem == 0:
        print(left)
    else:
        space = ' ' * (len(str(left)) + 1)
        print(f"{space}{rem}")
        print(f"{left} {'-' * len(str(den))}")
        print(f"{space}{den}")


def solve(n):
    num, den = 0, 1
    for k in range(1, n + 1):
        num = num * k + den * n
        den = den * k
        g = gcd(num, den)
        num //= g
        den //= g

    _print(num, den)


while True:
    try:
        N = int(input())
        solve(N)
    except:
        break
