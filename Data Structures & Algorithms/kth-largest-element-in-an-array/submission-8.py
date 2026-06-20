class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # index
        
        def quickselect(l, r):
            pivot, p = nums[r], l # arbitrary pivot, start from the left

            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[p] =  nums[p], nums[i]
                    p += 1
                    
            # put the pivot in the right index
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return quickselect(l, p - 1)
            elif p < k:
                return quickselect(p + 1, r)
            else:
                return nums[p]

        return quickselect(0, len(nums) - 1)
