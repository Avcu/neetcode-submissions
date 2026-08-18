class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            fElement = nums[0]

            perms = self.permute(nums[1:])
            resList = []
            for perm in perms:
                for i in range(len(perm)+1):
                    permCopy = perm.copy()
                    permCopy.insert(i, fElement)
                    resList.append(permCopy)
            return resList