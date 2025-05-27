import sys

input = sys.stdin.readline


def fail(arr: list[int]):
    f = [0] * len(arr)
    j = 0
    for i in range(1, len(arr)):
        while j > 0 and arr[i] != arr[j]:
            j = f[j - 1]
        if arr[i] == arr[j]:
            j += 1
            f[i] = j
    return f


def kmp(a: list[int], b: list[int], f: list[int]):
    j = 0
    for i in range(len(a)):
        while j > 0 and a[i] != b[j]:
            j = f[j - 1]
        if a[i] == b[j]:
            j += 1
            if j == len(b):
                return True
    return False


def to_diff(arr: list[int]):
    return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]


def main():
    N = int(input())
    songs = []

    for _ in range(N):
        _, *melody = map(int, input().split())
        songs.append(melody)

    l = int(input())
    target = list(map(int, input().split()))

    target_diff = to_diff(target)
    f = fail(target_diff)

    result = []

    for i in range(N):
        if len(songs[i]) < l:
            continue
        song_diff = to_diff(songs[i])
        if kmp(song_diff, target_diff, f):
            result.append(i + 1)

    if result:
        print(*result)
    else:
        print(-1)


if __name__ == '__main__':
    main()
