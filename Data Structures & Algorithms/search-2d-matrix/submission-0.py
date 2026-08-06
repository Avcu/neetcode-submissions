class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = 0
        row_r = len(matrix)-1

        while row_l <= row_r:
            row_middle = row_l + (row_r-row_l)//2
            
            # target cannot be in another row
            if matrix[row_middle][0] <= target and matrix[row_middle][-1] >= target:
                column_l = 0
                column_r = len(matrix[0])-1

                while column_l <= column_r:
                    column_middle = column_l + (column_r-column_l)//2
                    if matrix[row_middle][column_middle] == target:
                        return True
                    elif matrix[row_middle][column_middle] > target:
                        column_r = column_middle - 1
                    else:
                        column_l = column_middle + 1
                return False

            elif matrix[row_middle][0] > target:
                row_r = row_middle - 1
            else:
                row_l = row_middle + 1
        return False





        