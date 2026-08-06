class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen == 1:
            return s
        
        maxLen = 1
        maxString = s[0]
        for idx in range(sLen):
            ## odd number of chars
            l, r = idx-1, idx+1
            oddLen = 1
            oddStr = s[0]
            while l >= 0 and r < sLen:
                if s[l] == s[r]:
                    oddLen += 2
                    oddStr = s[l:r+1]
                else:
                    break
                l = l - 1
                r = r + 1
            
            ## event number of chars
            evenLen = 0
            evenStr = ""
            if idx > 0 and s[idx-1] == s[idx]:
                l, r = idx-2, idx+1
                evenLen += 2
                evenStr = s[idx-1:idx+1]
                while l >= 0 and r < sLen:
                    if s[l] == s[r]:
                        evenLen += 2
                        evenStr = s[l:r+1]
                    else:
                        break
                    l = l - 1
                    r = r + 1
            if oddLen > maxLen or evenLen > maxLen:
                if oddLen > evenLen:
                    maxLen = oddLen
                    maxString = oddStr
                else:
                    maxLen = evenLen
                    maxString = evenStr  
        return maxString



