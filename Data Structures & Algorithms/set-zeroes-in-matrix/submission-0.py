class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        firstRowZero, firstColumnZero = False, False

        firstColumn = [x[0] for x in matrix]   
        for j in firstColumn:
            if j == 0:
                firstColumnZero = True

        for i in matrix[0]:
            if i == 0:
                firstRowZero = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstColumnZero:
            for i in range(n):
                matrix[i][0] = 0
        if firstRowZero:
            for j in range(m):
                matrix[0][j] = 0
