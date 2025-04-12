l = int(input())
r = int(input())
k = int(input())

if k == 2:
    # 최소 합 3
    print(max(0, (r - max(l, 3) + 1)))
elif k == 3:
    # S = 3(x+d)
    # 최소 합 6
    start_val = max(l, 6)
    if start_val > r:
        print(0)
    else:
        count = (r // 3) - ((start_val - 1) // 3)
        print(count)
elif k == 4:
    # S = 2(2x+3d)수
    # 최소 합 10
    # 14++ 모든짝
    print(max(0, r // 2 - ((max(l, 14) - 1) // 2)) + (l <= 10 <= r))
elif k == 5:
    # S = 5x + 10d = 5(x+2d)
    # 최소 합 15
    start_val = max(l, 15)
    if start_val > r:
        print(0)
    else:
        count = (r // 5) - ((start_val - 1) // 5)
        print(count)
