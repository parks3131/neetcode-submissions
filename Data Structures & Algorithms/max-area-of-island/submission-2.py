class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        maxArea = 0

        def dfsArea(r,c):
            if r < 0 or r >= Rows or c < 0 or c >= Columns or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                row, col = r + dr, c + dc
                area+= dfsArea(row, col)
            return area

            
            
            

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfsArea(r,c))
        return maxArea