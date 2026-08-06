class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # XOR operation -> a ^ a = 0 and a ^ 0 = a
            result = result ^ num
        return result