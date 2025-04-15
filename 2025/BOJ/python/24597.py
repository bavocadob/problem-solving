def solve(s):
    doubled = s + s

    s_rev = s[::-1]
    if s_rev in doubled:
        return 1

    return 0


S = input().strip()
print(solve(S))
