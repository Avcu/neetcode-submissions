class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1]* n for _ in range(n+1)]

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i+1, j)

            if j == -1 or nums[j] < nums[i]:
                # try taking the number at i-th index
                memo[i][j] = max(memo[i][j], dfs(i+1, i) + 1)
            return memo[i][j]

        return dfs(0, -1)