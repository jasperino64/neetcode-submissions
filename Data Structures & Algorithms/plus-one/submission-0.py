class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(map(str,digits))
        n = int(s) + 1
        s = str(n)
        output = [int(c) for c in s]
        return output