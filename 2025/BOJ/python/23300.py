import sys

input = sys.stdin.readline


def backward(b: list[int], f: list[int]):
    global cur_page

    if not b:
        return

    page = b.pop()

    f.append(cur_page)
    cur_page = page


def go_forward(b: list[int], f: list[int]):
    global cur_page

    if not f:
        return

    page = f.pop()
    b.append(cur_page)
    cur_page = page


def compress(b: list[int]):
    if not b:
        return b

    new_back = list()
    new_back.append(b[0])

    for i in range(1, len(b)):
        if b[i] == b[i - 1]:
            continue

        new_back.append(b[i])

    return new_back


def access_page(b: list[int], f: list[int], next_page: int):
    global cur_page

    if cur_page != -1:
        b.append(cur_page)
    cur_page = next_page
    f.clear()


N, Q = map(int, input().split())

back = []
forward = []
cur_page = -1

for _ in range(Q):
    data = input().strip()

    Q = data[0]

    if Q == 'B':
        backward(back, forward)
    elif Q == 'F':
        go_forward(back, forward)
    elif Q == 'C':
        back = compress(back)
    else:
        _, n_page = data.split()
        access_page(back, forward, int(n_page))

print(cur_page)

if not back:
    print(-1)
else:
    print(*back[::-1])

if not forward:
    print(-1)
else:
    print(*forward[::-1])
