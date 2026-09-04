class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i == 1:
                return i
            if i in memo:
                return memo[i]

            res = 1
            for k in range(1,i//2+1):
                res = max(res, k * max(dfs(i-k), i-k))
            memo[i] = res
            return memo[i]
        
        return dfs(n)