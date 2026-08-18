class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def containsAll(dict1, dict2):
            for k, v in dict2.items():
                if k not in dict1 or dict1[k] < v:
                    return False
            return True


        countS = defaultdict(int)
        countT = defaultdict(int)

        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        totalChCount = len(countT.keys())

        # return if S does not have something that T has
        if not containsAll(countS, countT) or len(s) == 0:
            return ""

        minLen = float("inf")
        resStr = ""

        l, r = 0, 0
        matchingCount = 0
        countWindow = defaultdict(int)

        while r < len(s) and l <= r:
            # add the ch in the right index, and move the right index by one
            ch = s[r]
            countWindow[ch] = countWindow.get(ch, 0) + 1
            r += 1

            if ch in countT and countT[ch] == countWindow[ch]:
                matchingCount += 1

            # move the left index as long our condition satifies
            while matchingCount == totalChCount and l <= r:
                currLen = r - l

                if currLen < minLen:
                    minLen = currLen
                    resStr = s[l:r]

                ch = s[l]
                countWindow[ch] = countWindow.get(ch, 0) - 1
                if ch in countT and countT[ch] == countWindow[ch] + 1:
                    matchingCount -= 1
                l += 1
        return resStr