class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(i, isBought):
            if i >= len(prices):
                return 0

            if (i, isBought) in memo:
                return memo[(i, isBought)]
            
            skip = dfs(i+1, isBought)
            if not isBought:
                # buy the stock
                memo[(i, isBought)] = max(dfs(i+1, True)-prices[i], skip)
            
            if isBought:
                # sell the stock
                memo[(i, isBought)] = max(dfs(i+2, False)+prices[i], skip)

            return memo[(i, isBought)]

        return dfs(0, False)