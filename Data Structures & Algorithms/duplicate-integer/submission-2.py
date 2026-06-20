class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem={}
        for n in nums:
            if  n in mem:
                return True
            mem[n] = True
        return False