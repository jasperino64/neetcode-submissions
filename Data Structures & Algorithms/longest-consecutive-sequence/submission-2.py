class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)

        result = 0
        for n in nums:
            streak = 1
            curr = n
            while curr in store:
                result = max(result,streak)
                curr += 1
                streak += 1
        return result