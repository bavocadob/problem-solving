import sys

input = sys.stdin.readline


def manacher(nums: list[int]) -> list[int]:
    m = [-1] * (len(nums) * 2 + 1)

    for i in range(len(nums)):
        m[i * 2 + 1] = nums[i]

    rst = [0] * len(m)

    center = right = 0

    for i in range(1, len(m)):
        mirror = center * 2 - i

        if i < right:
            print(i, mirror, rst[mirror])
            rst[i] = min(rst[mirror], right - i)

        while i - rst[i] - 1 >= 0 and i + rst[i] + 1 < len(m) and m[i - rst[i] - 1] == m[i + rst[i] + 1]:
            rst[i] += 1

        if right < i + rst[i]:
            center = i
            right = i + rst[i]

    return rst


def query(left, right, man):
    s = (left + right) // 2
    mod = 0 if (right - left) % 2 == 1 else 1
    size = right - left + 1
    return man[s * 2 - mod] >= size


N = int(input())

A = list(map(int, input().split()))

dp = manacher(A)
M = int(input())

for _ in range(M):
    l, r = map(int, input().split())
    result = query(l, r, dp)
    print(1 if result else 0)

