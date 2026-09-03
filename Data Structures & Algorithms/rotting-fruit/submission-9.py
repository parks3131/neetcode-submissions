class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        fresh, Minutes = 0, 0
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                (row, col) = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh-=1
            Minutes+=1
        return Minutes if fresh == 0 else -1

