from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        maxTime = 0
        fresh = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(m):
            for  j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            lenQ = len(q)
            for idx in range(lenQ):
                i, j = q.popleft()
                for direction in directions:
                    iU = i + direction[0]
                    jU = j + direction[1]
                    if iU >= 0 and iU < m and jU >= 0 and jU < n and grid[iU][jU] == 1:
                        grid[iU][jU] = 2
                        q.append([iU, jU])
                        fresh -= 1
                
            maxTime += 1
        return maxTime if fresh == 0 else -1
