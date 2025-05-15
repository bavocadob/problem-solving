origin = input().rstrip()

T = input().rstrip()
char_to_i = {char: i for i, char in enumerate(T)}
i_to_char = {i: char for i, char in enumerate(T)}
dp = [0] * len(T)

for char in origin:
    if char not in char_to_i:
        continue

    if char_to_i[char] == 0:
        dp[0] += 1
    else:
        i = char_to_i[char]

        if dp[i - 1] == 0:
            continue

        dp[i - 1] -= 1
        dp[i] += 1

print(dp[len(T) - 1])
