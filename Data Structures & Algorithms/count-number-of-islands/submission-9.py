class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS Approach

        Rows, Columns = len(grid), len(grid[0])
        no_of_islands = 0
        directions = [[0,-1],[-1,0],[0,1],[1,0]]

        def dfs(r,c):
            if r < 0 or r >= Rows or c < 0 or c >= Columns or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr,nc)
        
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    dfs(r,c)
                    no_of_islands+=1
        return no_of_islands
