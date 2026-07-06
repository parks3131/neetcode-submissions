class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Columns = len(grid), len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        mins = 0
        fresh = 0
        q = deque()

        #we have to count the fresh fruit
        #we have to know all the 2

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                (row, col) = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < Rows and nc >= 0 and nc < Columns and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh-=1
            mins+=1
        
        return mins if fresh == 0 else -1

