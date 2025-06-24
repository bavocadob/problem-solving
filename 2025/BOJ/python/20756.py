MAX_H = 1000001


def sieve_h_primes(limit):
    is_h_composite = [False] * (limit + 1)

    for i in range(5, int(limit ** 0.5) + 1):
        if i % 4 != 1:
            continue

        for j in range(i, (limit // i) + 1):
            if j % 4 != 1:
                continue

            product = i * j
            if product > limit:
                break
            is_h_composite[product] = True

    h_primes = []
    for i in range(5, limit + 1, 4):
        if not is_h_composite[i]:
            h_primes.append(i)

    return h_primes


def get_semi(h_primes, limit):
    is_h_semi_prime = [False] * (limit + 1)

    for i in range(len(h_primes)):
        for j in range(i, len(h_primes)):
            product = h_primes[i] * h_primes[j]
            if product > limit:
                break
            is_h_semi_prime[product] = True

    return is_h_semi_prime


def get_counts(is_h_semi_prime, limit):
    cumulative_counts = [0] * (limit + 1)
    for i in range(1, limit + 1):
        cumulative_counts[i] = cumulative_counts[i - 1]
        if is_h_semi_prime[i]:
            cumulative_counts[i] += 1

    return cumulative_counts


def main():
    h_primes = sieve_h_primes(MAX_H)
    is_h_semi_prime = get_semi(h_primes, MAX_H)
    counts = get_counts(is_h_semi_prime, MAX_H)

    while True:

        N = int(input())

        if N == 0:
            break

        print(f"{N} {counts[N]}")


if __name__ == "__main__":
    main()
