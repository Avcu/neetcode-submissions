from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)]       # (effort, x, y)

        seen = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while minHeap:
            curEff, curX, curY = heappop(minHeap)
            if (curX, curY) in seen:
                continue
            seen.add((curX, curY))

            if curX == m-1 and curY == n-1:
                return curEff
            
            for d in directions:
                newX = curX + d[0]
                newY = curY + d[1]
                if newX >= 0 and newX < m and newY >= 0 and newY < n and (newX, newY):
                    diff = abs(heights[curX][curY] - heights[newX][newY])
                    heappush(minHeap, (max(curEff, diff), newX, newY))
