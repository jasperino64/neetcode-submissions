class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = collections.deque()
        fresh = 0
        time = 0
        def rot(r,c):
            nonlocal fresh
            if (r in range(ROWS) and c in range(COLS) and
                grid[r][c] == 1):
                grid[r][c] = 2
                fresh -= 1
                q.append([r,c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        print(fresh)
        
        if fresh == 0:
            return 0

        while fresh > 0 and q:

            for i in range(len(q)):
                r, c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
                
            time += 1
        return time if fresh == 0 else -1        

