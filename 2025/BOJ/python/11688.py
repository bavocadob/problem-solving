import math


def get_divisors(n):
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))


def main():
    a, b, L = map(int, input().split())

    lcm_ab = (a * b) // math.gcd(a, b)

    if L % lcm_ab != 0:
        print(-1)
        return

    k = L // lcm_ab

    div_ab = get_divisors(lcm_ab)

    for d in div_ab:
        c = k * d

        if math.gcd(lcm_ab, c) == d:
            print(c)
            return

    print(-1)


if __name__ == '__main__':
    main()
