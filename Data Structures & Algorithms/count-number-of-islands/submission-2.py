class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       Rows, Columns = len(grid), len(grid[0])
       num_island = 0 
       direction = [(1,0),(0,1),(0,-1),(-1,0)]
       def bfs(rows,cols):
        q = deque()
        q.append((rows,cols))
        grid[rows][cols] = "0"

        while q:
            (row,col) = q.popleft()
            for dr,dc in direction:
                nr, nc = row+dr, col+dc
                if nr<0 or nr >= Rows or nc<0 or nc >= Columns or grid[nr][nc] == "0":
                    continue
                grid[nr][nc] = "0"
                q.append((nr,nc))

       for i in range(Rows):
        for j in range(Columns):
            if grid[i][j] == "1":
                num_island+=1
                bfs(i,j)
       return num_island
