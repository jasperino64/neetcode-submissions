class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        result = 0
        l,r = 0, len(height) - 1
        maxL = height[0]
        maxR = height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                result += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                result += maxR - height[r]
        return result

