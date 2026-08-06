class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        arr = [0] * len(nums)

        for idx in range(len(nums)):
            if idx == 0:
                arr[idx] = nums[idx]
            elif idx == 1:
                arr[idx] = max(nums[idx-1], nums[idx])
            else:
                arr[idx] = max(arr[idx-1], arr[idx-2]+nums[idx])

        return max(arr[-1], arr[-2])

