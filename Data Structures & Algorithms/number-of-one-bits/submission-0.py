class Solution:
    def hammingWeight(self, n: int) -> int:
        one = 1
        res = 0
        for i in range(32):
            res += one & n
            n = n >> 1
        return res