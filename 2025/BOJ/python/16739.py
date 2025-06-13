import sys

input = sys.stdin.readline


def tokenize(filename):
    tokens = []
    i = 0
    n = len(filename)
    while i < n:
        char = filename[i]
        if char.isdigit():
            num_str = ''
            while i < n and filename[i].isdigit():
                num_str += filename[i]
                i += 1
            tokens.append(int(num_str))
        else:
            tokens.append(char)
            i += 1
    return tokens


def comp(t1, t2):
    for i in range(min(len(t1), len(t2))):
        val1 = t1[i]
        val2 = t2[i]

        is_num1 = isinstance(val1, int)
        is_num2 = isinstance(val2, int)

        if is_num1 != is_num2:
            return -1 if is_num1 else 1

        if val1 != val2:
            if is_num1:
                return val1 - val2
            else:
                return ord(val1) - ord(val2)

    return len(t1) - len(t2)


def main():
    N = int(input())

    s0 = input().rstrip()
    t0 = tokenize(s0)
    for _ in range(N):
        si = input().rstrip()
        ti = tokenize(si)
        if comp(ti, t0) < 0:
            print('-')
        else:
            print('+')


if __name__ == "__main__":
    main()
