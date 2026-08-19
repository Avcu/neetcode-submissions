class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums, []]
        else:
            resSet = set()
            nums.sort()
            firstElement = nums[0]
            restOfList = nums[1:]

            combWithoutFirstElement = self.subsetsWithDup(restOfList)

            for comb in combWithoutFirstElement:
                resSet.add(tuple(comb))
                comb.append(firstElement)
                resSet.add(tuple(comb))
            return [list(x) for x in resSet]