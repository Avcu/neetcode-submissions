class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        availSpots = [[0] * n for _ in range(n)]
        selected = []
        resIdx = []

        def mark(i, j, val):
            for idx in range(i+1, n):
                availSpots[idx][j] += val
            idx = 1
            while i + idx < n and j - idx >= 0:
                availSpots[i+idx][j-idx] += val
                idx += 1
            idx = 1
            while i + idx < n and j + idx < n:
                availSpots[i+idx][j+idx] += val
                idx += 1

        def dfs(i):
            if i == n:
                resIdx.append(selected.copy())
                return
            
            curAvailList = [j for j in range(n) if availSpots[i][j]==0]
            for curAvail in curAvailList:
                selected.append((i, curAvail))
                mark(i, curAvail, 1)

                dfs(i+1)
                selected.pop()
                mark(i, curAvail, -1)

        dfs(0)

        output = []
        for solution in resIdx:
            board = []
            for row, col in solution:
                board.append("." * col + "Q" + "." * (n - col - 1))
            output.append(board)

        return output







