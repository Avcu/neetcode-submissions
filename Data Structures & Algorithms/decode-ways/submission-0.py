class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s[0] == "0" else 1
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        
        for idx in range(1, len(s)+1):
            if s[idx-1] != "0":
                dp[idx] += dp[idx-1]
            if idx != 1:
                if s[idx-2] == "1" or (s[idx-2] == "2" and s[idx-1] in ["0", "1", "2", "3", "4", "5", "6"]):
                    dp[idx] += dp[idx-2]
        return dp[-1]
                    

