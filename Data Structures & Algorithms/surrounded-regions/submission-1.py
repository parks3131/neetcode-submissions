class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #gonna do dfs and convert all O touches the bundary and make it 
        #to a T then convert all remaining O to X and T to O
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        Rows, Columns = len(board), len(board[0])

        def dfs(r,c):
            if board[r][c] != "O":
                return
            board[r][c] = "T"
            q = deque()
            q.append((r,c))
            while(q):
                (rows, cols) = q.popleft()
                for dr, dc in directions:
                    nr, nc = rows+dr, cols+dc
                    if nr < 0 or nr >= Rows or nc < 0 or nc >= Columns or board[nr][nc] != "O":
                        continue
                    q.append((nr,nc))
                    board[nr][nc] = "T"

            

        for r in range(Rows):
            dfs(r,0)
            dfs(r,Columns-1)
        for c in range(Columns):
            dfs(0,c)
            dfs(Rows-1,c)
        
        for r in range(Rows):
            for c in range(Columns):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"