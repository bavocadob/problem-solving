import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    a_blocks = []
    for _ in range(N):
        t, d = map(int, input().split())
        a_blocks.append([t, d])

    M = int(sys.stdin.readline())
    b_blocks = []
    for _ in range(M):
        t, d = map(int, input().split())
        b_blocks.append([t, d])

    i = N - 1
    j = M - 1
    carry = 0
    temp_result = []

    while i >= 0 or j >= 0 or carry > 0:
        t_a, d_a = a_blocks[i] if i >= 0 else (0, 0)
        t_b, d_b = b_blocks[j] if j >= 0 else (0, 0)

        if t_a == 0 and t_b == 0:
            if carry > 0:
                temp_result.append([1, carry])
            break

        size = 0
        if t_a > 0 and t_b > 0:
            size = min(t_a, t_b)
        elif t_a > 0:
            size = t_a
        else:  # t_b > 0
            size = t_b

        s = d_a + d_b + carry
        res_d = s % 10
        new_carry = s // 10

        temp_result.append([1, res_d])

        if size > 1:
            s2 = d_a + d_b + new_carry
            res_d2 = s2 % 10
            final_carry = s2 // 10

            if temp_result and temp_result[-1][1] == res_d2:
                temp_result[-1][0] += size - 1
            else:
                temp_result.append([size - 1, res_d2])
            carry = final_carry
        else:
            carry = new_carry

        if i >= 0:
            a_blocks[i][0] -= size
            if a_blocks[i][0] == 0:
                i -= 1
        if j >= 0:
            b_blocks[j][0] -= size
            if b_blocks[j][0] == 0:
                j -= 1

    result = []

    while temp_result:
        t, d = temp_result.pop()

        if t == 0:
            continue

        if result and result[-1][1] == d:
            result[-1] = (result[-1][0] + t, d)
        else:
            result.append((t, d))

    print(len(result))
    for t, d in result:
        print(t, d)


def main():
    K = int(input())
    for t in range(1, K + 1):
        print(f'Data Set {t}:')
        solve()
        print()


if __name__ == "__main__":
    main()
