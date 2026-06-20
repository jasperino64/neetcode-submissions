class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        # Top down
        N = len(coins)
        coins.sort()
        dp = [[-1]* (amount + 1) for i in range(N + 1)]

        def dfs(i, a):
            if a == amount:
                return 1
            if i == len(coins):
                return 0
            if a > amount:
                return 0
            if dp[i][a] != -1:
                return dp[i][a]

            res = dfs(i+1, a)
            res += dfs(i, a + coins[i])

            dp[i][a] = res
            return res
        return dfs(0, 0)


            
