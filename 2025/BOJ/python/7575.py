import sys
from typing import List

input = sys.stdin.readline


def failure(arr: List[int]) -> List[int]:
    f = [0] * len(arr)

    j = 0

    for i in range(1, len(arr)):
        while j > 0 and arr[i] != arr[j]:
            j = f[j - 1]

        if arr[i] == arr[j]:
            j += 1
            f[i] = j

    return f


def kmp(s: List[int], target: List[int], f: List[int]) -> bool:
    j = 0

    for i in range(len(s)):

        while j > 0 and s[i] != target[j]:
            j = f[j - 1]
        if s[i] == target[j]:
            j += 1
            if j == len(target):
                return True

    return False


def main():
    N, K = map(int, input().split())

    programs = []

    for _ in range(N):
        m = int(input())

        program = list(map(int, input().split()))
        programs.append(program)

    for i in range(len(programs[0]) - K + 1):
        pattern = programs[0][i:i + K]
        pattern_rev = pattern[::-1]

        f = failure(pattern)
        f_rev = failure(pattern_rev)
        flag = True
        for j in range(1, N):
            program = programs[j]
            if not (kmp(program, pattern, f) or kmp(program, pattern_rev, f_rev)):
                flag = False
                break

        if flag:
            print('YES')
            return

    print('NO')


if __name__ == '__main__':
    main()
