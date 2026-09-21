class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = {}
        if n < m:
            return 0

        def dfs(i, j):
            if i == n:
                if j < m:
                    return 0
                if j == m:
                    return 1
            if j == m:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]

            # look for matching char
            take = 0
            if s[i] == t[j]:
                take = dfs(i+1, j+1)

            skip = dfs(i+1, j)
            memo[(i, j)] = take + skip
            return memo[(i, j)]

        return dfs(0, 0)