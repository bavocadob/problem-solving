from collections import defaultdict


def check(a, b):
    if len(a) != len(b):
        return False

    for key, value in b.items():
        if key not in a:
            return False
        if a[key] != value:
            return False
    return True


g, s = map(int, input().split())

word = input().rstrip()

a_dict = defaultdict(int)

for char in word:
    a_dict[char] += 1

ans = 0

b_dict = defaultdict(int)

S = input().rstrip() + ' '

for i in range(g):
    b_dict[S[i]] += 1

for i in range(g, s + 1):
    if check(a_dict, b_dict):
        ans += 1

    prev = S[i - g]
    cur = S[i]
    b_dict[prev] -= 1
    b_dict[cur] += 1

    if b_dict[prev] == 0:
        b_dict.pop(prev)

print(ans)
