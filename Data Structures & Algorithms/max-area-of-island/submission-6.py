class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        max_Area = 0


        def bfs(rows, cols):
            Area = 1
            Directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            q = deque()
            q.append((rows, cols))
            grid[rows][cols] = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in Directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= Rows or nc >= Columns or grid[nr][nc] == 0:
                            continue
                        grid[nr][nc] = 0
                        Area+=1
                        q.append((nr, nc))
            return Area

        
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    max_Area = max(max_Area, bfs(r, c))
        
        return max_Area

        