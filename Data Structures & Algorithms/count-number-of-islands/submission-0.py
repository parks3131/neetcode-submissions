class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows,Columns = len(grid),len(grid[0])
        island = 0



        def bfs(r,c):
            adjacent_list = [[0,1],[1,0],[0,-1],[-1,0]]
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            
            while(q):
                row,col = q.popleft()
                for ar,ac in adjacent_list:
                    nr,nc = ar+row,ac+col
                    if  nr<0 or nr>=Rows or nc<0 or nc>=Columns or grid[nr][nc] == "0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    bfs(r,c)
                    island+=1
        
        return island