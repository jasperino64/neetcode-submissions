class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        items = list(counts.items())
        print(items)
        items.sort(key=lambda x: x[1])
        items.reverse()
        result = [items[i][0] for i in range(k)]
        return result