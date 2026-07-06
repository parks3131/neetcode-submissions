class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        fresh = 0
        directions = [[0,-1], [-1, 0], [0, 1], [1, 0]]
        q = deque()
        minutes = 0

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                (r, c) = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or grid[nr][nc] != 1:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh-=1
            minutes+=1
        return -1 if fresh > 0 else minutes

    
        
        