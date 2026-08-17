class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                chLeftRemoved = s[l+1:r+1]
                chRightRemoved = s[l:r]
                return chLeftRemoved == chLeftRemoved[::-1] or chRightRemoved == chRightRemoved[::-1]
        return True