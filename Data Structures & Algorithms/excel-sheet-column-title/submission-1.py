class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        else:
            columnNumber = columnNumber - 1
            curVal = columnNumber % 26
            return self.convertToTitle(columnNumber // 26) + chr(curVal+ord('A'))