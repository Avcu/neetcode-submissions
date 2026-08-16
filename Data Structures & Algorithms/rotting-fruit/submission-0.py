from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        maxTime = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(m):
            for  j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        
        while q:
            [i, j, time] = q.popleft()
            for direction in directions:
                iU = i + direction[0]
                jU = j + direction[1]
                if iU >= 0 and iU < m and jU >= 0 and jU < n and grid[iU][jU] == 1:
                    q.append([iU, jU, time+1])
                    grid[iU][jU] = 2
                    maxTime = max(maxTime, time+1)
                
        for i in range(m):
            for  j in range(n):
                if grid[i][j] == 1:
                    return -1
        return maxTime
