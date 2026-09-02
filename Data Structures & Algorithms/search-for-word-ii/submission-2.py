class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        path = set()
        res = set()
        def dfs(node, x, y, word):
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] not in node.children or (x, y) in path:
                return

            path.add((x,y))
            node = node.children[board[x][y]]
            word += board[x][y]
            if node.isEnd:
                res.add(word)

            for x_, y_ in directions:
                xNew = x + x_
                yNew = y + y_
                dfs(node, xNew, yNew, word)
            path.remove((x, y))

        root = TrieNode()
        for w in words:
            root.addWord(w)

        for i in range(n):
            for j in range(m):
                path = set()
                dfs(root, i, j, "")

        return list(res)