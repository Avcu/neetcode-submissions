class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        resCount = 0
        leftIdx = 0

        for idx in range(len(s)):
            if s[idx] in charDict:
                leftIdx = max(charDict[s[idx]] + 1, leftIdx)
            
            charDict[s[idx]] = idx
            currLen = idx - leftIdx + 1
            if currLen > resCount:
                resCount = currLen
        return resCount

