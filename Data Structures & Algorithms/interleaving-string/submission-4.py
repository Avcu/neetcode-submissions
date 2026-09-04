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
            ite = 0
            while i+ite < len(s1) and s3[curLen+ite] == s1[i+ite]:
                ite += 1
                res = res or dfs(i+ite, j)

            # try taking next char from s2
            ite = 0
            while j+ite < len(s2) and s3[curLen+ite] == s2[j+ite]:
                ite += 1
                res = res or dfs(i, j+ite)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
