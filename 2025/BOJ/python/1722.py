def solve_1(k):
    e = list(range(1, N + 1))
    k -= 1
    result = []

    for i in range(N, 0, -1):
        idx = k // factorial[i - 1]
        result.append(e.pop(idx))
        k %= factorial[i - 1]

    return result


def solve_2(perm):
    e = list(range(1, N + 1))
    rst = 0

    for i in range(N):
        pos = e.index(perm[i])
        rst += pos * factorial[N - i - 1]
        e.pop(pos)

    return rst + 1


N = int(input())
Q, *nums = map(int, input().split())

factorial = [1] * (N + 1)

for i in range(1, N + 1):
    factorial[i] = factorial[i - 1] * i

if Q == 1:
    print(*solve_1(nums[0]))
else:
    print(solve_2(nums))
