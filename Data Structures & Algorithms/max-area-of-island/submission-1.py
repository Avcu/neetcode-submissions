class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.currArea = 0

        def visitNeighbors(grid, row, column):
            grid[row][column] = 0
            self.currArea += 1
            if row > 0 and grid[row-1][column] == 1:
                visitNeighbors(grid, row-1, column)
            if column > 0 and grid[row][column-1] == 1:
                visitNeighbors(grid, row, column-1)
            if row < len(grid)-1 and grid[row+1][column] == 1:
                visitNeighbors(grid, row+1, column)
            if column < len(grid[0])-1 and grid[row][column+1] == 1:
                visitNeighbors(grid, row, column+1)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    self.currArea = 0
                    # mark all the 1s on this island as 0
                    visitNeighbors(grid, row, column)
                    if self.currArea > maxArea:
                        maxArea = self.currArea
        return maxArea