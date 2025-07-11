import sys

input = sys.stdin.readline


def main():
    N, X = map(int, input().split())

    activities = [False] * (200_001 + X)

    for _ in range(N):
        s, d = map(int, input().split())

        for i in range(s, s + d + 1):
            activities[i] = True

    ans_time = 0
    ans_cnt = float('inf')

    for i in range(480 + 1):
        cnt = 0
        for j in range(i, len(activities), X):
            if activities[j]:
                cnt += 1

        if ans_cnt > cnt:
            ans_cnt = cnt
            ans_time = i

    print(ans_time, ans_cnt)


if __name__ == '__main__':
    main()
