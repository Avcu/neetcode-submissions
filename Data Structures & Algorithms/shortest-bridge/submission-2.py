from collections import deque 

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        setOne = set()

        n = len(grid)
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def explore(i, j, visitedSet):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1 or (i, j) in visitedSet:
                return
            else:
                visitedSet.add((i, j))
                for x, y in directions:
                    explore(i+x, j+y, visitedSet)

        def bfs():
            res = 0
            q = deque(setOne)

            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for x, y in directions:
                        ni, nj = i+x, j+y
                        if ni < 0 or ni >= n or nj < 0 or nj >= n or (ni, nj) in setOne:
                            continue
                        if grid[ni][nj] == 1:
                            return res
                        q.append((ni, nj))
                        setOne.add((ni, nj))
                res += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    explore(i, j, setOne)
                    print(setOne)
                    return bfs()