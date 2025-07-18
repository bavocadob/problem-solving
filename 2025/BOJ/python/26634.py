import math


def count_divisors(num):
    if num <= 0:
        return 0
    cnt = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num // i != i:
                cnt += 2
            else:
                cnt += 1
    return cnt


def main():
    n = int(input())

    ans = 0

    divs_of_n = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs_of_n.add(i)
            divs_of_n.add(n // i)

    for d in divs_of_n:
        target = d - 1

        if target < 6:
            continue

        divisors = count_divisors(target)
        excluded = {1, target}
        if target % 2 == 0:
            excluded.add(target // 2)

        cnt = divisors - len(excluded)

        if cnt > 0:
            ans += cnt

    print(ans)


if __name__ == '__main__':
    main()