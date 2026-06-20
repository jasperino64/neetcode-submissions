class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair of (index, height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # current height is shorter
                previndex,prevheight = stack.pop()
                maxArea = max(maxArea, prevheight * (i - previndex))
                start = previndex
            stack.append((start,h))

        for i,h in stack: # heights that reach the end
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea