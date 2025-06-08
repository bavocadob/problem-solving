# dict.txt => 문제에 첨부

words = []

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


def solve():
    grid = []
    for _ in range(5):
        grid.append(input().split())

    word_trie = Trie()
    for word in words:
        word_trie.insert(word)
        
    found_words = set()
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def dfs(x, y, current_node, current_word, visited):
        if current_node.is_end_of_word:
            found_words.add(current_word)

        if not current_node.children:
            return

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                next_char = grid[nx][ny]
                if next_char in current_node.children:
                    visited[nx][ny] = True
                    dfs(nx, ny, current_node.children[next_char], current_word + next_char, visited)
                    visited[nx][ny] = False

    for r in range(5):
        for c in range(5):
            char = grid[r][c]
            if char in word_trie.root.children:
                v = [[False] * 5 for _ in range(5)]
                v[r][c] = True
                dfs(r, c, word_trie.root.children[char], char, v)

    print(len(found_words))


solve()
