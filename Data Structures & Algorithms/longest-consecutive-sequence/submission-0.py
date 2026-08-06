class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)

        maxLen = 0
        for num in setNums:
            if num-1 in setNums:
                continue
            else:
                currLen = 1
                while num + currLen in setNums:
                    currLen += 1
                if currLen > maxLen:
                    maxLen = currLen     
        return maxLen
