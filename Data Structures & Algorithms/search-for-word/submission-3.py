class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Columns = len(board), len(board[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        

        def dfs(rows,cols,i):
            if i == len(word):
                return True
            if rows<0 or cols<0 or rows>= Rows or cols >= Columns or board[rows][cols] != word[i] :
                return False
            board[rows][cols] = "#"
            res = (dfs(rows,cols+1,i+1) or dfs(rows,cols-1,i+1)
                    or dfs(rows-1,cols,i+1) or dfs(rows+1,cols,i+1))
            board[rows][cols] = word[i]
            return res
            
                
            

        for rows in range(Rows):
            for cols in range(Columns):
                if dfs(rows,cols,0):
                    return True

        return False