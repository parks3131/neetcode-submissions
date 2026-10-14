class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs approach
        Rows, Columns = len(grid), len(grid[0])
        island = 0

        def dfs(rows, cols):
            if rows >= Rows or rows < 0 or cols >= Columns or cols < 0 or grid[rows][cols] != "1":
                return
            grid[rows][cols] = "0"
            dfs(rows - 1, cols)
            dfs(rows + 1, cols)
            dfs(rows, cols - 1)
            dfs(rows, cols + 1)

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island+=1
        return island
        
        