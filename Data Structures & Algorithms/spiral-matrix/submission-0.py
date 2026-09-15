class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        resList = []
        while left < right and top < bottom:
            for i in range(left, right):
                resList.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                resList.append(matrix[i][right-1])
            right -= 1

            if right == left or top == bottom:
                break

            for i in range(right-1, left-1, -1):
                resList.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                resList.append(matrix[i][left])
            left += 1

        return resList
            