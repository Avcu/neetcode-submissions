class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multipAll = 1
        zeroExists = False
        doubleZeroExists = False
        for num in nums:
            if num != 0:
                multipAll *= num
            else:
                if zeroExists:
                    doubleZeroExists = True
                zeroExists = True

        
        
        if doubleZeroExists:
            return [0] * len(nums)
        if zeroExists:
            resultList = []
            for num in nums:
                if num != 0:
                    resultList.append(0)
                else:
                    resultList.append(multipAll)
            return resultList

        resultList = []
        for num in nums:
            resultList.append(multipAll//num)
        return resultList