import sys

input = sys.stdin.readline
N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

ans = 0
for i in range(1, N - 1):
    ans = max(ans,
              abs(nums[i - 1] + nums[N - 1] - 2 * nums[i]),
              abs(nums[0] + nums[N - i] - 2 * nums[N - i - 1])
              )

print(ans)
