class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plusOneList = [0] * (len(digits) + 1)

        carryOver = 0
        for idx in range(1, len(digits)+1):
            currDigit = digits[-idx]
            if idx == 1:
                if currDigit == 9:
                    currDigit = 0
                    carryOver = 1
                else:
                    currDigit += 1
                
            else:
                if currDigit == 9 and carryOver == 1:
                    currDigit = 0
                    carryOver = 1
                else:
                    if carryOver == 1:
                        currDigit += 1
                        carryOver = 0
            plusOneList[-idx] = currDigit
        if carryOver == 1:
            plusOneList[0] = 1
            return plusOneList
        return plusOneList[1:]
            
        