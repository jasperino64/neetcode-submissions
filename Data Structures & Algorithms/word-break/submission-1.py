class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Top down
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if ((i+len(word)) <= len(s) and word == s[i: i + len(word)]):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False

            return memo[i]
            
        
        return dfs(0)

        # Bottom up
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]