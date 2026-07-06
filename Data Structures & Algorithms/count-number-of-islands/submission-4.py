class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        Rows, Columns = len(grid), len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]


        #we need a queue to put the ones in and we need to check 
        #all four direction and collect those ones in the queue
        #key thing we should do is as we encounter ones make it 0
        #so never add it unwantedly again

        def bfs(r,c):
            grid[r][c] == "0"
            q = deque()
            q.append((r,c))
            while(q):
                (row,col) = q.popleft()
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nr >= Rows or nc < 0 or nc >= Columns or grid[nr][nc] == "0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
                    
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    bfs(r,c)
                    num_island+=1
        return num_island

