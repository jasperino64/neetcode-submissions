class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 0
        for _ in range(n):
            tmp = one
            one += two
            two = tmp
        
        return one