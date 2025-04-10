s = input().rstrip()

jaum = {'r', 'R', 's', 'e', 'f', 'a', 'q', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g'}
moum = {'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'y', 'n', 'b', 'm', 'l'}
double_jaum = {'rt', 'sw', 'sg', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'qt'}

double_moum_to_moum = {'hk': 'h', 'ho': 'h', 'hl': 'h', 'nj': 'n', 'np': 'n', 'nl': 'n', 'ml': 'm'}

for before, after in double_moum_to_moum.items():
    s = s.replace(before, after)

ans = 0
for i in range(1, len(s) - 2):
    if s[i] in jaum and s[i - 1] in moum and s[i + 1] in moum:
        ans += 1
    elif s[i:i + 2] in double_jaum:
        if s[i - 1] in moum and s[i + 2] in moum:
            ans += 1

if s[-2] in jaum:
    if s[-3] in moum and s[-1] in moum:
        ans += 1
print(ans)
