class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdxDict = defaultdict(int)

        for idx in range(len(s)):
            lastIdxDict[s[idx]] = idx
        
        print(lastIdxDict)

        resList = []
        startIdx, lastIdx = 0, 0
        size = 0

        for idx in range(len(s)):
            lastIdx = max(lastIdx, lastIdxDict[s[idx]])
            size = lastIdx-startIdx+1

            if lastIdx == idx:
                resList.append(size)
                startIdx, lastIdx = idx+1, idx+1
        return resList
