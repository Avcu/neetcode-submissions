class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums, []]
        else:
            firstElement = nums[0]
            restOfList = nums[1:]
            combWithoutFirstElement = self.subsets(restOfList)
            combWithFirstElement = []
            for comb in combWithoutFirstElement:
                newComb = comb.copy()
                newComb.append(firstElement)
                combWithFirstElement.append(newComb)
            return combWithoutFirstElement + combWithFirstElement