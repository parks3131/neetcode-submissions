class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Columns = len(board), len(board[0])

        def dfs(i, r, c):
            if len(word) == i:
                return True
            if r < 0 or r >= Rows or c < 0 or c >= Columns or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            res = dfs(i+1,r-1,c) or dfs(i+1,r+1,c) or dfs(i+1,r,c-1) or dfs(i+1,r,c+1)
            board[r][c] = word[i]
            return res

        for r in range(Rows):
            for c in range(Columns):
                if dfs(0, r, c):
                    return True
        return False  