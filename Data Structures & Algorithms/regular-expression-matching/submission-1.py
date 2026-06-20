class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = {}

        def dfs(i, j):
            if j == n:
                return i == m

            if (i,j) in dp:
                return dp[i,j]

            match = i < m and (p[j] == s[i] or p[j] == ".")
            if ((j + 1) < n and p[j + 1] == "*"):
                dp[i, j] = (dfs(i, j + 2) or # don't use *
                            match and dfs(i + 1, j)) # use *
                return dp[i, j]
            
            if match:
                dp[i, j] = dfs(i + 1, j + 1)
                return dp[i, j]
            
            dp[i, j] = False
            return False

        return dfs(0,0)
            
