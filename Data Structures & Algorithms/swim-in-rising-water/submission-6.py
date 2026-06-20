class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        heap = [[grid[0][0], 0, 0]]
        visit.add((0,0))

        while heap:
            t, r, c = heapq.heappop(heap)            
            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                if (newr < 0 or newc < 0 or newr == N or newc == N or
                    (newr, newc) in visit):
                    continue
                visit.add((newr, newc))
                heapq.heappush(heap, [max(t,grid[newr][newc]), newr, newc])

