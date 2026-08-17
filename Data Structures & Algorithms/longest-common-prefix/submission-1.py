class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resStr = ""

        minLen = len(strs[0])
        for currStr in strs:
            minLen = min(minLen, len(currStr))

        for idx in range(minLen):
            currCh = strs[0][idx]
            for currStr in strs:
                if currCh != currStr[idx]:
                    return resStr
            
            resStr += currCh
        return resStr