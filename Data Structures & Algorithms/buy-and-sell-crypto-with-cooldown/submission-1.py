class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key = (i, buying), val = max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            key = (i, buying)
            if key in dp:
                return dp[key]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[key] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[key] = max(sell, cooldown)

            return dp[key]
        return dfs(0, True)