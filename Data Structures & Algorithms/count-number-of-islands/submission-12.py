class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        island = 0


        def dfs(r, c):
            if r < 0 or r >= Rows or c < 0 or c >= Columns or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island+=1
        return island