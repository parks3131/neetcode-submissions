class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        max_Area = 0


        def dfs(rows, cols):
            if rows < 0 or rows >= Rows or cols < 0 or cols >= Columns or grid[rows][cols] == 0:
                return 0
            grid[rows][cols] = 0
            return 1 + dfs(rows + 1, cols) + dfs(rows - 1, cols) + dfs(rows, cols - 1) + dfs(rows, cols + 1)
            
        
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    max_Area = max(max_Area, dfs(r, c))
        
        return max_Area

        