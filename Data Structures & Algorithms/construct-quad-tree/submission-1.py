"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def allSameCheck(grid, x1, y1, x2, y2):
            # checks if all grid[x][y] are the same for x1 <= x <= x2 and y1 <= y <= y2
            firstVal = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if firstVal != grid[i][j]:
                        return False
            return True
        
        def dfs(grid, x1, y1, x2, y2):
            if allSameCheck(grid, x1, y1, x2, y2):
                newNode = Node()
                newNode.val = grid[x1][y1]
                newNode.isLeaf = 1
                return newNode
            else:
                newNode = Node()
                newNode.val = 1
                newNode.isLeaf = 0
                newNode.topLeft = dfs(grid, x1, y1, (x1+x2)//2, (y1+y2)//2)
                newNode.topRight = dfs(grid, x1, (y1+y2)//2, (x1+x2)//2, y2)
                newNode.bottomLeft = dfs(grid, (x1+x2)//2, y1, x2, (y1+y2)//2)
                newNode.bottomRight = dfs(grid, (x1+x2)//2, (y1+y2)//2, x2, y2)
                return newNode
        
        return dfs(grid, 0, 0, len(grid), len(grid))



        