class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        print(Map)

        for c in s:
            if c not in Map:
                stack.append(c)
                continue

            if not stack or Map[c] != stack[-1]:
                return False
            stack.pop()
        return len(stack) == 0