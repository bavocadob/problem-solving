import re


def solve(expression):
    if expression == '0':
        return 'W'

    terms = re.findall(r'([+-]?\d*)x|([+-]?\d+)', expression)

    a, b = 0, 0

    for coeff, constant in terms:
        if coeff:
            a = int(coeff)
        elif constant:
            b = int(constant)
    if a == -2:
        int_a_str = '-xx'
    elif a != 0:
        int_a = a // 2
        int_a_str = f'{int_a}xx' if int_a != 1 else 'xx'
    else:
        int_a_str = ''

    if b != 0:
        if b == 1:
            int_b_str = 'x' if int_a_str == '' else '+x'
        elif b == -1:
            int_b_str = '-x'
        else:
            int_b_str = f'{b}x' if b > 0 and int_a_str == '' else f'+{b}x' if b > 0 else f'{b}x'
    else:
        int_b_str = ''

    result = f'{int_a_str}{int_b_str}+W'

    return result


exp = input().strip()
print(solve(exp))
