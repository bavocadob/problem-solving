def check(a, b):
    checked = 0

    while a > 0:
        digit = a % 10
        if checked & (1 << digit):
            return False
        checked |= (1 << digit)
        a //= 10

    while b > 0:
        digit = b % 10
        if checked & (1 << digit):
            return False
        checked |= (1 << digit)
        b //= 10

    return True


N = int(input())

flag = False
for i in range(1, min(87654, N) + 1):
    target = N - i
    if check(i, target):
        flag = True
        print(i, '+', target)
        break

if not flag:
    print(-1)
