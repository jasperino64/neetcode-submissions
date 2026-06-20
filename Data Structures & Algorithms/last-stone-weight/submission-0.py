class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-x for x in stones]
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            s1 = -heapq.heappop(self.maxHeap)
            s2 = -heapq.heappop(self.maxHeap)
            s = s1 - s2
            if s > 0:
                heapq.heappush(self.maxHeap,-s)
        if self.maxHeap:
            return -self.maxHeap[0]
        return 0