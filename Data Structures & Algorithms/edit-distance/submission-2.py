class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j

            if (i, j) in memo:
                return memo[(i, j)]

            res = float('inf')
            if word1[i] == word2[j]:
                res = min(res, dfs(i+1, j+1))

            # try removing (ignore the char at index i)
            res = min(res, dfs(i+1, j) + 1)
            # try adding
            res = min(res, dfs(i, j+1) + 1)
            # try replacing 
            res = min(res, dfs(i+1, j+1) + 1)

            memo[(i, j)] = res
            return memo[(i, j)]
            
        return dfs(0, 0)