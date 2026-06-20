class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.big = [] # min heap

    def addNum(self, num: int) -> None:
        if self.big and num > self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.small) > len(self.big) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        
        if len(self.big) > len(self.small) + 1:
            val = heapq.heappop(self.big)
            heapq.heappush(self.small, -val)


    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.small) > len(self.big):
            return - self.small[0]
        else:
            return (self.big[0] - self.small[0]) /2.0
        