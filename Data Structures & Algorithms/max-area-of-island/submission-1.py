class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        maxArea = 0

        def bfsArea(r,c):
            grid[r][c] = 0
            area = 1
            q = deque()
            q.append((r,c))
            while q:
                (row, col) = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or grid[nr][nc] == 0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    area+=1
            return area

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfsArea(r,c))
        return maxArea