class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap, (-dist, x, y))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [[x,y] for d,x,y in minHeap]