class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        n, m = len(s), len(p)
        
        def dfs(i, j):
            if j == m:
                return i == n

            if (i, j) in memo:
                return memo[(i, j)]


            first_match = (
                i < n and
                (p[j] == s[i] or p[j] == ".")
            )
            res = False
            if j + 1 < m and p[j + 1] == "*":
                # use the * zero times
                res = res or dfs(i, j+2)
                if first_match:
                    # use the * pattern
                    res = res or dfs(i+1, j)
            else:
                if first_match:
                    res = res or dfs(i+1, j+1)

            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dfs(0, 0)
