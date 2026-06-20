class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # n,k in [1...100]
        for u, v, w in times:
            adj[u].append((v,w))
        
        visit = set()
        heap = [[0, k]]

        time = 0
        while heap:
            w1, v1 = heapq.heappop(heap)
            if v1 in visit:
                continue

            visit.add(v1)
            time = w1
            print(v1, n)
            for v2, w2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(heap, [w1+w2, v2])
        
        return time if len(visit) == n else -1