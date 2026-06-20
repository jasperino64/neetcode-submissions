class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        drs= [0,1]

        for i in range(len(s)):
            for dr in drs:
                l = i
                r = i + dr
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1
                    l-=1
                    r+=1
        return res