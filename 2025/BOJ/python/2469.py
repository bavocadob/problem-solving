import sys

input = sys.stdin.readline


def solve(org, tar):
    rst = []

    for i in range(1, len(org)):
        if org[i - 1] == tar[i] and org[i] == tar[i - 1]:
            rst.append('-')
        else:
            rst.append('*')

    for i in range(len(org) - 1):
        if rst[i] == '-':
            org[i], org[i + 1] = org[i + 1], org[i]

    if org == tar:
        return ''.join(rst)
    else:
        return 'x' * (len(org) - 1)


K = int(input())
N = int(input())

target = list(input().strip())
original = [chr(ord('A') + i) for i in range(K)]

rev = []

flag = False
for _ in range(N):
    temp = list(input())
    if not flag:
        if temp[0] == '?':
            flag = True
            continue

        for i in range(K - 1):
            if temp[i] == '-':
                original[i], original[i + 1] = original[i + 1], original[i]
    else:
        rev.append(temp)

while rev:
    temp = rev.pop()

    for i in range(K - 1):
        if temp[i] == '-':
            target[i], target[i + 1] = target[i + 1], target[i]

print(solve(original, target))
