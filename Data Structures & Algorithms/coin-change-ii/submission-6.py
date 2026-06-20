class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Optimized
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(len(coins) -1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount+1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]


        # Bottom up
        N = len(coins)
        coins.sort()
        dp = [[0]* (amount + 1) for i in range(N + 1)]
        
        for i in range(N + 1):
            dp[i][0] = 1
        
        for i in range(N-1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
        return dp[0][amount]
        
        
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


            
