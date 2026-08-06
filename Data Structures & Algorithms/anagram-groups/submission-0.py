class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        def createAnagramListFromStr(string: str):
            myList = [0] * 26
            for ch in string:
                idx = ord(ch) - ord('a')
                myList[idx] += 1
            return myList

        for currString in strs:
            currList = createAnagramListFromStr(currString)
            anagramDict[tuple(currList)].append(currString)
        
        return list(anagramDict.values())


