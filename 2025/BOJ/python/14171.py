import sys
from collections import defaultdict

input = sys.stdin.readline


def atoi(char):
    return ord(char) - ord('A')


def make_hash(word):
    return atoi(word[0]) * 26 + atoi(word[1])


def make_pair(city, state):
    c_hash = make_hash(city)
    s_hash = make_hash(state)
    return HASH_MUL * c_hash + s_hash


def reverse_hash(val):
    l = val // HASH_MUL
    r = val % HASH_MUL

    return r * HASH_MUL + l


HASH_MUL = 26 * 26


def main():
    N = int(input())
    hash_count = defaultdict(int)
    for _ in range(N):
        city, state = input().split()
        val = make_pair(city[:2], state)
        hash_count[val] += 1

    ans = 0

    for hash_val, cnt in hash_count.items():
        reverse_val = reverse_hash(hash_val)

        if reverse_val == hash_val:
            continue

        if reverse_val in hash_count:
            ans += cnt * hash_count[reverse_val]

    print(ans // 2)


if __name__ == '__main__':
    main()
