from collections import deque 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        oCoordinates = set()
        oQueue = deque()

        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for x in range(m):
            if board[x][0] == "O":
                 oCoordinates.add((x, 0))
                 oQueue.append([x, 0])
            if board[x][n-1] == "O":
                 oCoordinates.add((x, n-1))
                 oQueue.append([x, n-1])

        for x in range(n):
            if board[0][x] == "O":
                 oCoordinates.add((0, x))
                 oQueue.append([0, x])
            if board[m-1][x] == "O":
                 oCoordinates.add((m-1, x))
                 oQueue.append([m-1, x])
        
        while oQueue:
            [currX, currY] = oQueue.popleft()
            for direction in directions:
                newX = currX + direction[0]
                newY = currY + direction[1]

                if newX >= 0 and newX < m and newY >= 0 and newY < n:
                    if board[newX][newY] == "O" and (newX, newY) not in oCoordinates:
                        oCoordinates.add((newX, newY))
                        oQueue.append([newX, newY])

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O" and (x,y) not in oCoordinates:
                    board[x][y] = 'X'