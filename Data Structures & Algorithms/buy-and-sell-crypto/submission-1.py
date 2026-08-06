class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for price in prices:
            if price > low:
                currProfit = price-low
                if currProfit > profit:
                    profit = currProfit
            elif price < low:
                low = price
            else:
                continue
        return profit