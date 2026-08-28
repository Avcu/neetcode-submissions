class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        for idx in range(n):
            dp[idx][idx] = True

        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if j-1 == i:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
        return sum(sum(r) for r in dp)