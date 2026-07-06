class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        maxArea = 0

        def findMaxArea(r, c):
            if r < 0 or r >= Rows or c < 0 or c >= Columns or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            area+=findMaxArea(r - 1, c) + findMaxArea(r + 1, c) + findMaxArea(r, c - 1) + findMaxArea(r, c + 1)
            return area

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, findMaxArea(r, c))
        return maxArea