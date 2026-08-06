class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNumbers = set()
        for num in nums:
            if num in uniqueNumbers:
                return True
            else:
                uniqueNumbers.add(num)
        return False
        