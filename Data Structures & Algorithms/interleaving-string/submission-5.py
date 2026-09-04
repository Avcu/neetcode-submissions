class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        memo = {}

        def dfs(i, j):
            if i >= len(s1) or j >= len(s2):
                if i == len(s1):
                    return s2[j:] == s3[i+j:]
                else:
                    return s1[i:] == s3[i+j:]
            
            if (i, j) in memo:
                return memo[(i, j)]

            curLen = i + j
            res = False
            # try taking next char from s1
            if i < len(s1) and s3[curLen] == s1[i]:
                res = res or dfs(i+1, j)

            # try taking next char from s2
            if j < len(s2) and s3[curLen] == s2[j]:
                res = res or dfs(i, j+1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
