class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0 ], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        maxarea =  0
        def dfs(r, c):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visit or grid[r][c] == 0):
                return 0
            
            visit.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                maxarea = max(maxarea, dfs(r,c))
        return maxarea