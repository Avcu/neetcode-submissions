class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, total):
            if i == len(coins) or total > amount:
                return float('inf')
            if total == amount:
                return 0

            if (i, total) in memo:
                return memo[(i, total)]

            take = dfs(i, total + coins[i]) + 1
            skip = dfs(i+1, total)

            memo[(i, total)] = min(take, skip)
            return memo[(i, total)]

        return -1 if dfs(0, 0) == float('inf') else dfs(0,0)
