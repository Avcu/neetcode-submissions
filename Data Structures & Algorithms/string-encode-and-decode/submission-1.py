class Solution:

    def encode(self, strs: List[str]) -> str:
        myString = ""
        for currStr in strs:
            currLen = len(currStr)
            myString += str(currLen) + "#" + currStr
        return myString

    def decode(self, s: str) -> List[str]:
        myList = []

        index = s.find("#")
        while index != -1:
            currLen = int(s[:index])
            myList.append(s[index+1:index+currLen+1])
            s = s[index+currLen+1:]
            index = s.find("#")
        return myList
