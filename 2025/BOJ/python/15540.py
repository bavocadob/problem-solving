import sys

input = sys.stdin.readline


def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, is_p in enumerate(is_prime) if is_p]


def binary_search(primes, target, n):
    left, right = 0, n
    rst = -1

    while left <= right:
        mid = (left + right) // 2
        if primes[mid] <= target:
            rst = mid
            left = mid + 1
        else:
            right = mid - 1

    return rst


def solve(m, a, b, primes):
    max_area = 0
    ans_p, ans_q = 0, 0

    for i in range(len(primes) - 1, -1, -1):
        q = primes[i]

        if q * q < max_area:
            break

        p_upper = min(q, m // q)
        p_lower = (q * a + b - 1) // b

        if p_upper < p_lower:
            continue

        p_idx = binary_search(primes, p_upper, i)

        if p_idx != -1:
            p = primes[p_idx]
            if p >= p_lower:
                area = p * q
                if area > max_area:
                    max_area = area
                    ans_p = p
                    ans_q = q

    return ans_p, ans_q


def main():
    MAX_M = 100000
    primes = get_primes(MAX_M)

    while True:
        m, a, b = map(int, input().split())

        if m == 0 and a == 0 and b == 0:
            break

        p, q = solve(m, a, b, primes)
        print(p, q)


if __name__ == '__main__':
    main()
