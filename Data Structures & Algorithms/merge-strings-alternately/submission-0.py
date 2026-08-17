class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        curr1, curr2 = 0, 0
        resStr = ""
        while curr1 < len(word1) and curr2 < len(word2):
            resStr += word1[curr1] + word2[curr2]
            curr1 += 1
            curr2 += 1
        if curr1 == len(word1):
            resStr += word2[curr2:]
        if curr2 == len(word2):
            resStr += word1[curr1:]
        return resStr