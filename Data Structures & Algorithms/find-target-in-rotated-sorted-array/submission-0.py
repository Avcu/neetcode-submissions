class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        minIdx = 0
        while l <= r:
            mid = (l+r) // 2
            midVal = nums[mid]

            if midVal <= nums[(mid-1)%len(nums)] and midVal <= nums[(mid+1)%len(nums)]:
                minIdx = mid
                break
            else:
                if nums[l] < nums[r] and midVal < nums[l]:
                    l = mid + 1
                elif nums[l] < nums[r] and midVal >= nums[l]:
                    r = mid - 1
                if nums[l] > nums[r] and midVal < nums[l]:
                    r = mid - 1
                elif nums[l] > nums[r] and midVal >= nums[l]:
                    l = mid + 1
        
        arr1 = nums[:minIdx]
        arr2 = nums[minIdx:]
        l, r = 0, len(arr1) - 1
        while l <= r:
            mid = (l+r) // 2
            midVal = arr1[mid]

            if midVal == target:
                return mid
            else:
                if midVal < target:
                    l = mid + 1
                else:
                    r = mid - 1

        l, r = 0, len(arr2) - 1
        while l <= r:
            mid = (l+r) // 2
            midVal = arr2[mid]

            if midVal == target:
                return mid + minIdx
            else:
                if midVal < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1