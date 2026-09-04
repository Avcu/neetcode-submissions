class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for idx in range(len(dp)):
            j = 1
            while j*j <=idx:
                dp[idx] = min(dp[idx], dp[idx-j*j]+1)
                j += 1
        
        return dp[-1]