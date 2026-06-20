class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Bottom up
        dp =[[float("inf")] * (n + 1) for i in range(m + 1)]

        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        dp = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i

            if (i,j) in dp:
                return dp[i,j]

            dp[i,j] = dfs(i + 1, j + 1)
            if word1[i] != word2[j]:
                dp[i,j] = 1 + min(dp[i,j], dfs(i + 1, j), dfs(i, j + 1))
            return dp[i, j]
            
        
        return dfs(0, 0)