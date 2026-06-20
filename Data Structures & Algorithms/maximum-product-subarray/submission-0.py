class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        for n in nums:
            tmp = min(n, n*curMin, n*curMax)
            curMax = max(n, n*curMin, n*curMax)
            curMin = tmp
            res = max(res, curMin, curMax)
            
        return res