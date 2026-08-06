class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniqueNumbers = set()
        for num in nums:
            if num in uniqueNumbers:
                return num
            else:
                uniqueNumbers.add(num)