import sys

input = sys.stdin.readline


def check():
    for i in range(4):
        for j in range(8):

            cur = byte_arr[0][i] & (1 << (8 - j - 1))

            for k in range(N):
                compare = byte_arr[k][i] & (1 << (8 - j - 1))

                if compare ^ cur:
                    return (4 - i - 1) * 8 + (8 - j)

    return 0


def print_ip(target):
    rst = []

    for i in range(4):
        temp = 0

        for j in range(8):
            bit_pos = (4 - i - 1) * 8 + (8 - j)
            if bit_pos <= cidr:
                break

            temp |= target[i] & (1 << (8 - j - 1))

        rst.append(str(temp))

    print('.'.join(rst))


N = int(input())
byte_arr = []

for _ in range(N):
    address = list(map(int, input().split('.')))
    byte_arr.append(address)

cidr = check()

print_ip(byte_arr[0])
print_ip([255, 255, 255, 255])
