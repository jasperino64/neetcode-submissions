class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for i in range(len(prices)):
            profit = max(profit, prices[i]-low)
            low = min(low, prices[i])
        
        return profit