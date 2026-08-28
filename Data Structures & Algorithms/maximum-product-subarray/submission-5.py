class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = [-10**3] * len(nums)
        dpMin = [10**3] * len(nums)
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        for idx in range(1, len(nums)):
            maxMultip = max(nums[idx]*dpMax[idx-1], nums[idx]*dpMin[idx-1])
            minMultip = min(nums[idx]*dpMax[idx-1], nums[idx]*dpMin[idx-1])
            dpMax[idx] = max(nums[idx], maxMultip)
            dpMin[idx] = min(nums[idx], minMultip)
        return max(dpMax)