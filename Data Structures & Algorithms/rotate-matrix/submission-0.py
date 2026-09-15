class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # reverse the first list
        matrix.reverse()

        # swap (i,j) with (j,i) which is transposing
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
