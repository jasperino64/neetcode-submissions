class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIndex, stackT = stack.pop()
                result[stackIndex] = i - stackIndex

            stack.append((i,t))
        
        return result