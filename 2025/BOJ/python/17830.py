import sys

input = sys.stdin.readline


def solve():
    n, bit = input().split()
    n = int(n)
    first_q = bit.find('?')
    first_one = bit.find('1')
    total_q = bit.count('?')
    total_one = bit.count('1')
    length = len(bit)

    if first_q == -1 and first_one == -1:
        max_digits = 1
    elif first_q == -1 or first_one == -1:
        max_digits = n + length - max(first_q, first_one)
    else:
        max_digits = n + length - min(first_q, first_one)
    if total_q + total_one == 1:
        max_digits -= 1

    if first_one == -1:
        min_digits = 1
    else:
        min_digits = n + length - first_one
    if total_one == 1:
        min_digits -= 1

    print(max_digits, min_digits)


T = int(input())
for _ in range(T):
    solve()
