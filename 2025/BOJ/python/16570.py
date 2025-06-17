import sys

input = sys.stdin.readline


def fail(arr):
    n = len(arr)
    f = [0] * n

    j = 0

    for i in range(1, n):
        while j > 0 and arr[i] != arr[j]:
            j = f[j - 1]

        if arr[i] == arr[j]:
            j += 1
            f[i] = j

    return f


def main():
    N = int(input())

    nums = list(map(int, input().split()))[::-1]
    f = fail(nums)

    ans, cnt = 0, 0

    for i in range(N):
        if f[i] > ans:
            ans, cnt = f[i], 1
        elif f[i] == ans:
            cnt += 1

    if ans:
        print(ans, cnt)
    else:
        print(-1)


if __name__ == '__main__':
    main()
