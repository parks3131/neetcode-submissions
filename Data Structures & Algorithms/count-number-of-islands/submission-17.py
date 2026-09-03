class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs approach
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                for i in range(len(q)):
                    (rows, cols) = q.popleft()
                    for dr, dc in directions:
                        nr = rows + dr
                        nc = cols + dc
                        if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or grid[nr][nc] == "0":
                            continue
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        Rows, Columns = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        island = 0

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island+=1
        return island

        
        