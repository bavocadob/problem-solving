def solve(grid):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            if val == 0:
                empties.append((r, c))
            else:
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + (c // 3)].add(val)

    def backtrack(idx=0):
        if idx == len(empties):
            return True
        r, c = empties[idx]
        b = (r // 3) * 3 + (c // 3)
        for num in range(1, 10):
            if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                grid[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if backtrack(idx + 1):
                    return True

                grid[r][c] = 0
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)
        return False

    return backtrack()


def check(grid):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            if val != 0:
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + (c // 3)].add(val)

    for i in range(9):
        if len(rows[i]) != 9 or len(cols[i]) != 9 or len(boxes[i]) != 9:
            return False

    return True


N = int(input())
for _ in range(N):
    g = [[int(ch) for ch in input().strip()] for _ in range(9)]

    if solve(g) and check(g):
        for row in g:
            print(''.join(str(d) for d in row))
    else:
        print("Could not complete this grid.")

    print()
