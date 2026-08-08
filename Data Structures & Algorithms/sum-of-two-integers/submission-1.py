class Solution:
    def getSum(self, a: int, b: int) -> int:
        resSum = 0
        carryOver = 0
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF
        for idx in range(32):
            valA = a & 1
            valB = b & 1
            if carryOver == 1:
                if valA == 1 and valB == 1:
                    currVal = 1
                elif (valA == 1 and valB == 0) or (valA == 0 and valB == 1):
                    currVal = 0
                else:
                    currVal = 1
                    carryOver = 0
            else:
                if valA == 1 and valB == 1:
                    carryOver = 1
                    currVal = 0
                elif (valA == 1 and valB == 0) or (valA == 0 and valB == 1):
                    currVal = 1
                else:
                    currVal = 0
            a = a >> 1
            b = b >> 1
            resSum = resSum | (currVal << idx)
        if resSum > maxInt:
            resSum = ~(resSum ^ mask)
        return resSum