class Solution:
    def longestPalindrome(self, s: str) -> str:
        drs = [0,1]
        res = ""
        resLen = 0
        for i in range(len(s)):
            for dr in drs:
                l = i
                r = i + dr
                while l >=0 and r < len(s) and s[l] == s[r]:
                    currlen = r-l+1
                    if currlen > resLen:
                        resLen = currlen
                        res = s[l:r+1]
                    l-=1
                    r+=1
        
        return res