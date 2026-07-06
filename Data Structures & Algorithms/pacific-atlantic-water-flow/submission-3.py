class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Columns = len(heights), len(heights[0])
        Pacific, Atlantic = set(), set()
        res = []

        def dfs(r,c,visit,preheight):
            if (r,c) in visit or r < 0 or r >= Rows or c < 0 or c >= Columns or preheight > heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])

        for i in range(Rows):
            dfs(i,0,Pacific,heights[i][0])
            dfs(i,Columns-1,Atlantic, heights[i][Columns-1])
        
        for i in range(Columns):
            dfs(0,i,Pacific,heights[0][i])
            dfs(Rows-1,i,Atlantic, heights[Rows-1][i])

        for row in range(Rows):
            for col in range(Columns):
                if (row,col) in Pacific and (row,col) in Atlantic:
                    res.append([row,col])
        return res
