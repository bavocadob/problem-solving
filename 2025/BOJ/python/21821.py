import sys

input = sys.stdin.readline
K, N = map(int, input().split())
members = list(input().split())
member = {name: 0 for name in members}
member['zzzzzzzzzz'] = -1

for _ in range(K):
    group = []
    temp_group = []
    prev = 'zzzzzzzzzz'

    for author in list(input().split()):
        author = author
        if author > prev:
            temp_group.append(author)
        else:
            group.append(temp_group)
            temp_group = [author]
        prev = author
    else:
        group.append(temp_group)

    cur = 0
    while group:
        temp = group.pop()
        _min, _max = int(1e9), 0
        for a in temp:
            _min = min(_min, member[a])

        for a in temp:
            member[a] = member[a] - _min + cur
            _max = max(_max, member[a])

        cur = _max + 1

for cur_member in members:
    for comp_member in members:
        if cur_member == comp_member:
            print('B', end='')
        elif member[cur_member] > member[comp_member]:
            print('0', end='')
        elif member[cur_member] < member[comp_member]:
            print('1', end='')
        else:
            print('?', end='')
    print()
