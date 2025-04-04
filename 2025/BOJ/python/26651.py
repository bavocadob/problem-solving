MID = 'BCDEFGHIJKLMNOPQRSTUVWXY'


def solve(X):
    l, r = 0, 0

    if X == 0:
        print('THEREISNOCOWLEVEL')
        return

    while True:
        if l >= r:
            if (r + 1) * l > X:
                break
            else:
                r += 1
        else:
            if (l + 1) * r > X:
                break
            else:
                l += 1

    print('A' * l, end='')
    print(MID, end='')
    print('Z' * r, end='')

    last = X - (l * r)
    if last:
        print('A' * last, end='')
        print(MID, end='')
        print('Z')


N = int(input())
solve(N)
