class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        sumNums = 0
        for n in nums:
            sumNums += n
            prefixSum.append(sumNums)

        res = 0
        myDict = defaultdict(int)
        for curSum in prefixSum:
            if curSum - k in myDict:
                res += myDict[curSum-k]
            myDict[curSum] += 1
        return res