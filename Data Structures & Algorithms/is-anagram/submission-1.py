from collections  import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        print(countS)
        print(countT)
        for c in countS:
            if countS[c] != countT[c]:
                return False
        
        return True
