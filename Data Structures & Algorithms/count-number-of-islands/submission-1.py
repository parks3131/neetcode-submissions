class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        island = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        


        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                (rows, columns) = q.popleft()
                for dr, dc in directions:
                    nr, nc = rows+dr, columns+dc

                    if nr < 0 or nr >= Rows or nc < 0 or nc>= Columns or grid[nr][nc] == "0":
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr,nc))

        for row in range(Rows):
            for col in range(Columns):
                if grid[row][col] == "1":
                    bfs(row,col)
                    island+=1
        return island
