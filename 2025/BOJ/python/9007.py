import sys

input = sys.stdin.readline


def upper_bound(arr: list[int], t):
    l, r = 0, len(arr) - 1

    rst = arr[-1]
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == t:
            return t
        elif arr[mid] > t:
            r = mid - 1
            rst = arr[mid]
        else:
            l = mid + 1

    return rst


def lower_bound(arr: list[int], t):
    l, r = 0, len(arr) - 1

    rst = arr[0]
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == t:
            return t
        elif arr[mid] > t:
            r = mid - 1

        else:
            l = mid + 1
            rst = arr[mid]

    return rst


T = int(input())

for _ in range(T):
    K, N = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    sums = set()
    sums2 = set()
    for i in range(N):
        for j in range(N):
            sums.add(A[i] + B[j])
            sums2.add(C[i] + D[j])

    sums = sorted(list(sums))

    ans = int(1e9)
    for cur in sums2:
        target = K - cur

        if target <= 0:
            if abs(ans - K) > abs(cur + sums[0] - K):
                ans = cur + sums[0]
        else:
            up, low = upper_bound(sums, target), lower_bound(sums, target)

            if abs(ans - K) > abs(cur + up - K):
                ans = cur + up
            elif abs(ans - K) == abs(cur + up - K):
                ans = min(ans, cur + up)

            if abs(ans - K) > abs(cur + low - K):
                ans = cur + low
            elif abs(ans - K) == abs(cur + low - K):
                ans = min(ans, cur + low)

    print(ans)
