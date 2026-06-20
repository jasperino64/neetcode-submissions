class Solution:
    def longestPalindrome(self, s: str) -> str:
        starts = [[0,0],[0,1]]
        res = ""
        for i in range(len(s)):
            for dl,dr in starts:
                l = i
                r = i + dr
                while l >=0 and r < len(s) and s[l] == s[r]:
                    currlen = r-l+1
                    if currlen > len(res):
                        res = s[l:r+1]
                    l-=1
                    r+=1
        
        return res