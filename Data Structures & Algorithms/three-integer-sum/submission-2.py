class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        nums.sort()
        for  i,n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = n + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    trips.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return trips
