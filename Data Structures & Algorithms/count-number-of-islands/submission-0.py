class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visitNeighbors(grid, row, column):
            grid[row][column] = '0'
            if row > 0 and grid[row-1][column] == '1':
                visitNeighbors(grid, row-1, column)
            if column > 0 and grid[row][column-1] == '1':
                visitNeighbors(grid, row, column-1)
            if row < len(grid)-1 and grid[row+1][column] == '1':
                visitNeighbors(grid, row+1, column)
            if column < len(grid[0])-1 and grid[row][column+1] == '1':
                visitNeighbors(grid, row, column+1)
            return grid

        islandCount = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    islandCount += 1
                    # mark all the 1s on this island as 0
                    grid = visitNeighbors(grid, row, column)
        return islandCount