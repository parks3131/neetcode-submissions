class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows, Columns = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r,c,visit,preheight):
            if (r,c) in visit or r<0 or c<0 or r == Rows or c == Columns or heights[r][c]<preheight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for i in range(Rows):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,Columns-1,atlantic,heights[i][Columns-1])
        
        for i in range(Columns):
            dfs(0,i,pacific,heights[0][i])
            dfs(Rows-1,i,atlantic,heights[Rows-1][i])

        for i in range(Rows):
            for j in range(Columns):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res
        