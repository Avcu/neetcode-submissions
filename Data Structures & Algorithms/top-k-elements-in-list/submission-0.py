class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        
        sortedNums = sorted(numDict.items(), key=lambda x: -x[1])

        resList = []
        for idx in range(k):
            resList.append(sortedNums[idx][0])
        return resList
