def make_dp_arr():
    arr = [0] * 1_000_001

    for i in range(10, 1_000_001):
        str_i = str(i)

        length = len(str_i)

        for l in range(1, length):
            if arr[i]:
                break
            for start in range(length - l + 1):
                temp = str_i[start:start + l]
                temp = int(temp)
                if temp == 0:
                    continue

                if arr[i - temp] == 0:
                    arr[i] = 1
                    break

    return arr


def solve(n, dp):
    ans = int(1e9)

    if dp[n] == 0:
        return -1

    str_n = str(n)

    length = len(str_n)

    for l in range(1, length):
        for start in range(length - l + 1):
            temp = str_n[start:start + l]
            temp = int(temp)
            if temp == 0:
                continue

            if dp[n - temp] == 0:
                ans = min(ans, temp)

    return ans


dp_arr = make_dp_arr()

N = int(input())

print(solve(N, dp_arr))
