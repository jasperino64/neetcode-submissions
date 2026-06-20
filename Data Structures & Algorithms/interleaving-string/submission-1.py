class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Top down
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            # dp[(i,j)] = False

            return False

        return dfs(0,0)

        # Bottom up
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] *(n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i+j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]