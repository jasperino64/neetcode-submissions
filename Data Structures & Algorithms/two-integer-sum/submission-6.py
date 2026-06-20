class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffIndexMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in diffIndexMap:
                return [diffIndexMap[diff], i]

            diffIndexMap[nums[i]] = i