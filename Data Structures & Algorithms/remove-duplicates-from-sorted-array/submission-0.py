class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        k = 0

        for num in nums:
            if num not in numSet:
                numSet.add(num)
                nums[k] = num
                k += 1
        return k