from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        pQueue = deque()
        pOcean = [[0] * n for _ in range(m)]
        for x in range(n):
            pOcean[0][x] = 1
            pQueue.append([0, x])
        for x in range(m):
            pOcean[x][0] = 1
            pQueue.append([x, 0])

        while pQueue:
            [currX, currY] = pQueue.popleft()
            for direction in directions:
                newX = currX + direction[0]
                newY = currY + direction[1]
                if newX >= 0 and newX < m and newY >= 0 and newY < n:
                    if pOcean[newX][newY] == 0 and heights[newX][newY] >= heights[currX][currY]:
                        pOcean[newX][newY] = 1
                        pQueue.append([newX, newY])
        
        aQueue = deque()
        aOcean = [[0] * n for _ in range(m)] 
        for x in range(n):
            aOcean[m-1][x] = 1
            aQueue.append([m-1, x])
        for x in range(m):
            aOcean[x][n-1] = 1
            aQueue.append([x, n-1])

        while aQueue:
            [currX, currY] = aQueue.popleft()
            for direction in directions:
                newX = currX + direction[0]
                newY = currY + direction[1]
                if newX >= 0 and newX < m and newY >= 0 and newY < n:
                    if aOcean[newX][newY] == 0 and heights[newX][newY] >= heights[currX][currY]:
                        aOcean[newX][newY] = 1
                        aQueue.append([newX, newY])

        resList = []
        for i in range(m):
            for j in range(n):
                if pOcean[i][j] == 1 and aOcean[i][j] == 1:
                    resList.append([i,j])
        return resList
        
        