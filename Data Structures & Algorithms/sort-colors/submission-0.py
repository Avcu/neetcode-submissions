class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        oneStartIdx, twoStartIdx = 0, 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                oneStartIdx += 1
                twoStartIdx += 1
            elif nums[idx] == 1:
                twoStartIdx += 1
            
        nums[:oneStartIdx] = [0] * oneStartIdx
        nums[oneStartIdx:twoStartIdx] = [1] * (twoStartIdx-oneStartIdx)
        nums[twoStartIdx:] = [2] * (len(nums)-twoStartIdx)
