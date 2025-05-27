import sys
input = sys.stdin.readline

INF = float('inf')
MAX_K = 31

def kmp(a, b):
    s = b + '#' + a
    lps = [0] * len(s)
    for i in range(1, len(s)):
        j = lps[i - 1]
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
        lps[i] = j

    return lps[-1]

# 입력
n, m = map(int, input().split())
m -= 1

names = []
lengths = []

for _ in range(n):
    s = input().strip()
    names.append(s)
    lengths.append(len(s))

# f[k][i][j] : i → j 로 2^k개 문자열 연결 시 최소 추가 길이
f = [[[INF] * n for _ in range(n)] for _ in range(MAX_K)]

# f[0] 초기화 (한 번 연결)
for i in range(n):
    for j in range(n):
        if i == j:
            # 자기 자신은 전체 길이-1까지 비교
            overlap = kmp(names[i], names[j][:-1])
        else:
            overlap = kmp(names[i], names[j])
        f[0][i][j] = lengths[j] - overlap


for k in range(1, MAX_K):
    for i in range(n):
        for j in range(n):
            for t in range(n):
                f[k][i][j] = min(f[k][i][j], f[k-1][i][t] + f[k-1][t][j])

dis = lengths[:]


for ff in f:
    print(ff)

for k in range(MAX_K):
    if (m >> k) & 1:
        tmp = [INF] * n
        for i in range(n):
            for j in range(n):
                tmp[j] = min(tmp[j], dis[i] + f[k][i][j])
        dis = tmp
        print(dis, k)

print(min(dis))
