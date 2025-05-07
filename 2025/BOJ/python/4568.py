import sys

input = sys.stdin.readline

t = 1
while True:
    line = input().rstrip()
    if line == '0':
        break

    cap, query = line.split()
    cap = int(cap)

    cache = []
    print(f'Simulation {t}')
    for ch in query:
        if ch != '!':
            if ch in cache:
                cache.remove(ch)
            cache.append(ch)
            if len(cache) > cap:
                cache.pop(0)
        else:
            print(''.join(cache))

    t += 1
