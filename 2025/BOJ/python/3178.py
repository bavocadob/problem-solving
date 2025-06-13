import sys

input = sys.stdin.readline
N, K = map(int, input().split())
words = [input() for _ in range(N)]

prefix_trie = {}
ans = 0

for word in words:
    current_node = prefix_trie
    for i in range(K):
        char = word[i]
        if char not in current_node:
            current_node[char] = {}
            ans += 1
        current_node = current_node[char]

suffix_trie = {}

for word in words:
    current_node = suffix_trie
    for i in range(2 * K - 1, K - 1, -1):
        char = word[i]
        if char not in current_node:
            current_node[char] = {}
            ans += 1
        current_node = current_node[char]

print(ans)
