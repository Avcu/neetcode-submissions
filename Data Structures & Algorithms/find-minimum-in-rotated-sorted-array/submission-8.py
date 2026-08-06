class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            middle = (l+r)//2
            middleVal = nums[middle]
            if middleVal <= nums[(middle-1)%len(nums)] and middleVal <= nums[(middle+1)%len(nums)]:
                return middleVal

            if nums[l] > nums[r] and middleVal >= nums[l]:
                l = middle + 1
            elif nums[l] > nums[r] and middleVal < nums[l]:
                r = middle - 1
            elif nums[l] < nums[r] and middleVal >= nums[l]:
                r = middle - 1
            elif nums[l] < nums[r] and middleVal < nums[l]:
                l = middle + 1