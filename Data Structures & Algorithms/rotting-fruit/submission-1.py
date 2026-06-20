from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = collections.deque()
        fresh = 0
        time = 0
        def rot(r,c):
            nonlocal fresh
            if (0 <= r < ROWS and 0 <= c < COLS and
                grid[r][c] == 1):
                grid[r][c] = 2
                fresh -= 1
                q.append([r,c])
        
        # Count # of fresh and put rotten fruit in the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        # print(fresh)
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    rot(row,col)
            time += 1
        return time if fresh == 0 else -1        

