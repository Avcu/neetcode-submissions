class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()

        def dfs(i, x, y):
            if i == len(word):
                return True
            if x < 0 or x >=n or y < 0 or y >= m or board[x][y] != word[i] or (x,y) in path:
                return False
            else:
                path.add((x,y))
                res = dfs(i+1, x-1, y) or dfs(i+1, x+1, y) or dfs(i+1, x, y-1) or dfs(i+1, x, y+1)
                path.remove((x,y))
                return res
        
        res = False
        for i in range(n):
            for j in range(m):
                res = res or dfs(0, i, j)
        return res
            
