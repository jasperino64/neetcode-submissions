class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count =  defaultdict(int)
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            
            # we need to maximize the window
            # res will only change when window and maxf changes
            # while (r-l+1) - maxf > k: # while invalid
            while (r-l+1) - max(count.values()) > k: # while invalid
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res