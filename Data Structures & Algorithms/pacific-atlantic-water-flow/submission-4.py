class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        Rows, Columns = len(heights), len(heights[0])
        res = []

        def dfs(r,c,visit,preheight):
            if r<0 or r >= Rows or c < 0 or c >= Columns or (r,c) in visit or preheight > heights[r][c]:
                return
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])

        for r in range(Rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,Columns-1,atlantic,heights[r][Columns-1])
        
        for c in range(Columns):
            dfs(0,c,pacific,heights[0][c])
            dfs(Rows-1,c,atlantic,heights[Rows-1][c])

        for r in range(Rows):
            for c in range(Columns):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res

