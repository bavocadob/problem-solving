l = int(input())
r = int(input())
k = int(input())

if k == 2:
    # 최소 합 3
    print(r - max(l, 3) + 1)
elif k == 3:
    # S = 3(x+d)
    # 최소 합 6
    start_val = max(l, 6)
    count = (r // 3) - ((start_val - 1) // 3)
    print(count)
elif k == 4:
    # S = 4x + 6d = 2(2x+3d)
    # 최소 합 10
    start_val = max(l, 10)
    count = (r // 2) - ((start_val - 1) // 2)
    if l <= 12 <= r:
        count -= 1
    print(count)
elif k == 5:
    # S = 5x + 10d = 5(x+2d)
    # 최소 합 15
    start_val = max(l, 15)
    count = (r // 5) - ((start_val - 1) // 5)
    print(count)
