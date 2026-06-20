class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for price in prices:
            profit = max(profit, price-low)
            low = min(low, price)
        
        return profit