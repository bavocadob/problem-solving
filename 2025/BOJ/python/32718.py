import bisect
import sys

input = sys.stdin.readline
N, K, T = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(N):
    nums[i] = nums[i] % K
A = list(map(int, input().split()))

nums.sort()

acc = 0

for a in A:
    acc += a
    acc %= K

    target = K - acc - 1
    idx = bisect.bisect_left(nums, target)
    if idx == N:
        ans = max((nums[0] + acc) % K, (nums[-1] + acc) % K)
    else:
        ans = max((nums[idx] + acc) % K, (nums[idx - 1] + acc) % K)

    print(ans, end=' ')
