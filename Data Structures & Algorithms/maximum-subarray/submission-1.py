class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        newList = []
        maxSum = nums[0]
        for idx in range(len(nums)):
            if idx == 0:
                newList.append(nums[0])
            else:
                newList.append(max(nums[idx], nums[idx]+newList[-1]))
        
            if newList[-1] > maxSum:
                maxSum = newList[-1]
        return maxSum
