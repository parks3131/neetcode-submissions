class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #first after encountering on we should do a traversal all the space of the 
        #specific island and also make sure those spaces are not visited already or later
        #then we need a no_of_islands to count the number of island
        #the traversal i am planning to use an breadth first search

        Rows, Columns = len(grid), len(grid[0])
        no_of_islands = 0
        directions = [[0,-1],[-1,0],[0,1],[1,0]]

        def dfs(row,col):
            q = deque()
            q.append((row,col))
            grid[row][col] = "0"
            while q:
                (r, c) = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or grid[nr][nc] == "0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        
        for r in range(Rows):
            for c in range(Columns):
                if grid[r][c] == "1":
                    dfs(r,c)
                    no_of_islands+=1
        return no_of_islands
