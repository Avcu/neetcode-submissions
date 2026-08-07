class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def createDictFromString(s:str):
            charDict = {}
            for ch in s:
                if ch in charDict:
                    charDict[ch] += 1
                else:
                    charDict[ch] = 1
            return charDict

        if len(s1) > len(s2):
            return False

        s1Dict = createDictFromString(s1)
        s2Dict = createDictFromString(s2[:len(s1)])
        if s1Dict == s2Dict:
            return True

        for idx in range(len(s1),len(s2)):
            if s2[idx] in s2Dict:
                s2Dict[s2[idx]] += 1
            else:
                s2Dict[s2[idx]] = 1

            removeIdx = idx - len(s1)
            if s2Dict[s2[removeIdx]] == 1:
                s2Dict.pop(s2[removeIdx])
            else:
                s2Dict[s2[removeIdx]] -= 1

            if s1Dict == s2Dict:
                return True

        return False