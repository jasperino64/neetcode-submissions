class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counts = defaultdict(int)
        freqs = [[] for i in range(len(nums)+1)]
        for n in nums:
            counts[n] += 1

        for n, c in counts.items():
            freqs[c].append(n)

        for i in range(len(freqs)-1, 0, -1):
            for n in freqs[i]:
                result.append(n)
                if len(result) == k:
                    return result
        # items = list(counts.items())
        # print(items)
        # items.sort(key=lambda x: x[1])
        # result = [x[0] for x in items[-k:]]
        # return result