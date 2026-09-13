class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        memo = {}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            curVal = matrix[i][j]
            res = 0

            for dr, dc in directions:
                if i+dr >= 0 and i+dr < n and j+dc >= 0 and j+dc < m and matrix[i+dr][j+dc] > matrix[i][j]:
                    res = max(res, 1+dfs(i+dr, j+dc))
            memo[(i, j)] = res
            return memo[(i, j)]

        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        return res+1