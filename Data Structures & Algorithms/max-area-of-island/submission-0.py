class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        max_length = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def bfs_count(r,c):
            count = 1
            q = deque()
            q.append((r,c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nr>=Rows or nc<0 or nc>=Columns or grid[nr][nc] == 0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    count+=1
            return count

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    max_length = max(max_length,bfs_count(r,c))
        return max_length
        