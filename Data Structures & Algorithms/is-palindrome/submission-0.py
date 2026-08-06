class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = re.sub(r'[^a-zA-Z0-9]', '', s)
        normalizedString = cleanString.lower()
        startIdx = 0
        endIdx = len(normalizedString) - 1
        
        while startIdx < endIdx:
            if normalizedString[startIdx] != normalizedString[endIdx]:
                return False
            else:
                startIdx += 1 
                endIdx -= 1

        return True
