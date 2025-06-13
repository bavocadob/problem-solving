import sys

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        rst = ''
        end = False
        for char in word:
            if char not in node.children:
                if not end:
                    rst += char
                    end = True

                next_node = TrieNode()
                node.children[char] = next_node
                node = next_node
            else:
                node = node.children[char]
                rst += char

        node.cnt += 1
        if rst == word:
            if node.cnt > 1:
                rst += str(node.cnt)

        return rst


trie = Trie()

N = int(input())

for _ in range(N):
    nickname = input().rstrip()
    alias = trie.add(nickname)
    print(alias)
