from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]       # (level, x, y)

        seen = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while minHeap:
            curLevel, curX, curY = heappop(minHeap)
            if (curX, curY) in seen:
                continue
            seen.add((curX, curY))

            if curX == n-1 and curY == n-1:
                return curLevel
            
            for d in directions:
                newX = curX + d[0]
                newY = curY + d[1]
                if newX >= 0 and newX < n and newY >= 0 and newY < n:
                    newLevel = max(curLevel, grid[newX][newY])
                    heappush(minHeap, (newLevel, newX, newY))