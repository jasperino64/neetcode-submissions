from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        array = []
        for n,count in freq.items():
            array.append([count, n])

        array.sort()
        return  [array[len(array)-1-i][1] for i in range(k)]