class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS approach
        Rows, Columns = len(grid), len(grid[0])
        Directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        islands = 0

        def bfs(rows, cols):
            q = deque()
            grid[rows][cols] = "0"
            q.append((rows, cols))

            while q:
                for i in range(len(q)):
                    (r, c) = q.popleft()
                    for dr, dc in Directions:
                        nr, nc = r + dr, c + dc
                        if nr >= 0 and nr < Rows and nc >= 0 and nc < Columns and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands+= 1
        return islands

        
        