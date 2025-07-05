import sys
from collections import Counter


def prime_factorization(num, primes):
    factors = Counter()
    while num > 1:
        prime = primes[num]
        factors[prime] += 1
        num //= prime
    return factors


def main():
    N, Q = map(int, input().split())

    prime_factors = list(range(N + 1))
    for i in range(2, int(N ** 0.5) + 1):
        if prime_factors[i] == i:
            for j in range(i * i, N + 1, i):
                if prime_factors[j] == j:
                    prime_factors[j] = i

    results = []
    for _ in range(Q):
        a, b = map(int, sys.stdin.readline().split())

        factors = prime_factorization(a, prime_factors)
        factors += prime_factorization(b, prime_factors)

        gcd = 1
        for prime, count in factors.items():
            power = count // 2
            if power:
                gcd *= (prime ** power)

        results.append(str(gcd))

    print(' '.join(results))


if __name__ == '__main__':
    main()
