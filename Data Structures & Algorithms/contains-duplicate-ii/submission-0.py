class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = defaultdict(int)
        minLen = float("inf")

        for curIdx in range(len(nums)):
            curNum = nums[curIdx]

            if curNum in myDict:
                diffIdx = abs(curIdx-myDict[curNum])
                minLen = min(minLen, diffIdx)
            myDict[curNum] = curIdx
        
        return minLen <= k