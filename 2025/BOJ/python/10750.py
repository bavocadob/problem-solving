S = input().strip().encode()  # 문자열을 바이트로 변환
T = input().strip().encode()
m = len(T)

stack = bytearray()

for ch in S:
    stack.append(ch)
    if len(stack) >= m and stack[-m:] == T:
        del stack[-m:]

print(stack.decode())
