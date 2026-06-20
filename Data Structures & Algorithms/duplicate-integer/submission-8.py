class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for x in nums:
            if x in numset:
                return True
            numset.add(x)

        return False