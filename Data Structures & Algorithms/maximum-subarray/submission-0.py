class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cursum = 0

        for n in nums:
            cursum = max(cursum, 0)
            cursum += n
            res = max(res,cursum)
        return res