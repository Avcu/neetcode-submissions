class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        x = abs(x)
        res = 0
        
        while x > 0:
            lastDigit = x % 10
            res = res+lastDigit
            x = int(x / 10)
            if x > 0:
                res = res * 10
        if res > 2**31-1 or res < -2**31:
            return 0 
        return -res if isNegative else res