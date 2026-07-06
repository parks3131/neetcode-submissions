class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Columns = len(board), len(board[0])

        def wordsearch(r,c,length):
            if length == len(word):
                return True
            if r < 0 or r >= Rows or c < 0 or c >= Columns or board[r][c] != word[length]:
                return False
            board[r][c] = "#"
            res = wordsearch(r - 1, c, length + 1) + wordsearch(r + 1, c, length + 1) + wordsearch(r, c - 1, length + 1) + wordsearch(r, c + 1, length + 1)
            board[r][c] = word[length]
            return res
        
        
        for r in range(Rows):
            for c in range(Columns):
                if board[r][c] == word[0]:
                    if wordsearch(r,c,0):
                        return True
        return False