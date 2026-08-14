class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounter = defaultdict(int)

        leftIdx = 0
        maxFrequency = 0

        maxLen = 0
        for rightIdx in range(len(s)):
            charCounter[s[rightIdx]] = charCounter.get(s[rightIdx], 0) + 1
            maxFrequency = max(maxFrequency, charCounter[s[rightIdx]])

            while (rightIdx-leftIdx+1) - maxFrequency > k:
                charCounter[s[leftIdx]] -= 1
                leftIdx += 1
            maxLen = max(maxLen, rightIdx-leftIdx+1)
        return maxLen
            



            