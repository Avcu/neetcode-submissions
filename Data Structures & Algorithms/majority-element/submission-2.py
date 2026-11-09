class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElement = nums[0]
        majFreq = 0

        elementDict = defaultdict(int)

        for num in nums:
            elementDict[num] += 1
            if elementDict[num] > majFreq:
                majElement = num
                majFreq = elementDict[num]
        return majElement
