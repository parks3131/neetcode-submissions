class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #track the O in the sides and track the connected Os to those Os on the sides
        #mark those as T and then completely make the all elements X only if its not T

        Rows, Columns = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= Rows or col < 0 or col >= Columns or board[row][col] != "O":
                return
            board[row][col] = "T"
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            

        for r in range(Rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][Columns - 1] == "O":
                dfs(r, Columns - 1)
        for c in range(Columns):
            if board[0][c] == "O":
                dfs(0, c)
            if board[Rows - 1][c] == "O":
                dfs(Rows - 1, c)
        
        for r in range(Rows):
            for c in range(Columns):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
