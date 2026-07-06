class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #height equal or lower required for the water flow
        #find a cell which can flow water to both oceans

        #first from each corner cell find which are cell reaches pacific and same for
        #atlantic
        #now find the common on both which means water can flow on both of it


        #I forgot the check of (r,c) in visit in base

        Rows, Columns = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def search(r, c, visit, preheight):
            if r < 0 or r >= Rows or c < 0 or c >= Columns or preheight > heights[r][c] or ((r,c) in visit):
                return
            visit.add((r,c))
            search(r-1,c,visit,heights[r][c])
            search(r+1,c,visit,heights[r][c])
            search(r,c-1,visit,heights[r][c])
            search(r,c+1,visit,heights[r][c])

        for r in range(Rows):
            search(r, 0, pacific, heights[r][0])
            search(r, Columns-1, atlantic, heights[r][Columns-1])
        for c in range(Columns):
            search(0,c,pacific, heights[0][c])
            search(Rows-1, c, atlantic, heights[Rows-1][c])
        
        for r in range(Rows):
            for c in range(Columns):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

    