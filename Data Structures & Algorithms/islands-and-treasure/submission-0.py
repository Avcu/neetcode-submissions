class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rowCnt = len(grid)
        columnCnt = len(grid[0])

        def search(grid, rowIdx, columnIdx, distance):
            if rowIdx < 0 or columnIdx < 0 or rowIdx == rowCnt or columnIdx == columnCnt:
                return None
            if grid[rowIdx][columnIdx] == -1:
                return None
            if grid[rowIdx][columnIdx] < distance:
                return None
            grid[rowIdx][columnIdx] = distance
            search(grid, rowIdx-1, columnIdx, distance+1)
            search(grid, rowIdx, columnIdx-1, distance+1)
            search(grid, rowIdx+1, columnIdx, distance+1)
            search(grid, rowIdx, columnIdx+1, distance+1)

        for rowIdx in range(rowCnt):
            for columnIdx in range(columnCnt):
                if grid[rowIdx][columnIdx] == 0:
                    search(grid, rowIdx, columnIdx, 0)
        
