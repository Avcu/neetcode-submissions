class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRowOrColumn(arr) -> bool:
            sudokuSet = set()
            for curr in arr:
                if curr != '.' and curr in sudokuSet:
                    return False
                elif curr not in sudokuSet:
                    sudokuSet.add(curr)
            return True
        def checkSquare(arr, row, column) -> bool:
            sudokuSet = set()
            for rowIdx in range(row, row+3):
                for columnIdx in range(column, column+3):
                    if arr[rowIdx][columnIdx] != '.' and arr[rowIdx][columnIdx] in sudokuSet:
                        return False
                    elif arr[rowIdx][columnIdx] not in sudokuSet:
                        sudokuSet.add(arr[rowIdx][columnIdx])
            return True

        resBool = True
        for idx in range(9):
            resBool = resBool and checkRowOrColumn(board[idx])
            columnArr = [row[idx] for row in board]
            resBool = resBool and checkRowOrColumn(columnArr)

        for i in range(3):
            for j in range(3):
                resBool = resBool and checkSquare(board, i*3, j*3)
        return resBool
