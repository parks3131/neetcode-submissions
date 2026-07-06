class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r >= Rows or c >= Columns or r < 0 or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r - 1,c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return
        Rows, Columns = len(grid), len(grid[0])
        islands = 0
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands+=1
        return islands