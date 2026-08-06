class Solution:

    def encode(self, strs: List[str]) -> str:
        myString = ""
        for currStr in strs:
            currLen = len(currStr)
            myString += "(" + str(currLen) + ")" + currStr
        return myString

    def decode(self, s: str) -> List[str]:
        myList = []

        index = s.find(")")
        while index != -1:
            currLen = int(s[1:index])
            myList.append(s[index+1:index+1+currLen])
            s = s[index+1+currLen:]
            index = s.find(")")
        return myList
