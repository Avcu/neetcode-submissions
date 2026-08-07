class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mult = 0
        for num in nums:
            mult = mult ^ num

        allMult = 0
        for num in range(len(nums)+1):
            allMult = allMult ^ num

        print(bin(mult))
        print(bin(allMult))
        res = 0
        for i in range(32):
            if (allMult & 1) != (mult & 1):
                res = res | (1 << i) 
            allMult = allMult >> 1
            mult = mult >> 1
        print(bin(res))
        return res
