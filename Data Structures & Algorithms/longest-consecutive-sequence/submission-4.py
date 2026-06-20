class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0

        for n in nums:
            streak = 1
            if n - 1 not in store:
                while n + streak in store:
                    streak += 1
            result = max(result,streak)
        return result