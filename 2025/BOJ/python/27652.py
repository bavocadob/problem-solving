import sys
from collections import defaultdict

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            node.count += 1

    def delete(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            node.count -= 1


def main():
    Q = int(input())

    trie_A = Trie()
    trie_B = Trie()

    for _ in range(Q):
        query = input().split()
        command = query[0]

        if command == 'add':
            target_set, s = query[1], query[2]
            if target_set == 'A':
                trie_A.add(s)
            else:
                trie_B.add(s[::-1])
        elif command == 'delete':
            target_set, s = query[1], query[2]
            if target_set == 'A':
                trie_A.delete(s)
            else:
                trie_B.delete(s[::-1])
        elif command == 'find':
            s = query[1]
            L = len(s)
            ans = 0

            suffix_counts = [0] * L
            node_b = trie_B.root
            for i in range(L - 1, 0, -1):
                char = s[i]
                if char not in node_b.children:
                    break
                node_b = node_b.children[char]
                suffix_counts[i] = node_b.count

            node_a = trie_A.root
            for i in range(L - 1):
                char = s[i]
                if char not in node_a.children:
                    break
                node_a = node_a.children[char]

                a = node_a.count
                b = suffix_counts[i + 1]

                ans += a * b

            print(ans)


if __name__ == '__main__':
    main()
