class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0
        for n in nums:
            streak = 1
            curr = n
            while curr + 1 in store:
                streak += 1
                curr += 1
            result = max(result, streak)
        
        return result

