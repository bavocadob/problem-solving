import sys

input = sys.stdin.readline
mark = {'!', '?', ',', '.'}


def is_of_korea_word(w: str):
    if w == 'Korea':
        return True

    if len(w) != 6 or not w.startswith('Korea') or w[-1] not in mark:
        return False

    return True


def capitalize_first_char(s):
    if not s:
        return s
    return s[0].upper() + s[1:]


def solve(s: str):
    temp_rst = []

    words = s.split()

    for word in words:
        if is_of_korea_word(word) and len(temp_rst) >= 2 and temp_rst[-1] == 'of' and temp_rst[-2][-1] not in mark:
            temp_rst.pop()
            temp = 'K-' + capitalize_first_char(temp_rst.pop())
            if word[-1] in mark:
                temp += word[-1]
            temp_rst.append(temp)
        else:
            temp_rst.append(word)
    rst = []

    for word in temp_rst[::-1]:
        if word == 'Korea':
            if rst:
                temp = rst.pop()
                rst.append('K-' + capitalize_first_char(temp))
            else:
                rst.append(word)
        else:
            rst.append(word)

    print(' '.join(rst[::-1]))


N = int(input())

for _ in range(N):
    sentence = input().rstrip()
    solve(sentence)
