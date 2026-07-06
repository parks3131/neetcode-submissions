class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column = len(matrix[0])
        row = len(matrix)
        
        if row == 1:
            return True if target in matrix[0] else False
        i = 1
        while(i < row):
            if target <= matrix[i][0]:
                return True if target in matrix[i-1] or target == matrix[i][0] else False
            i+=1
        
        for k in range(column):    #This is for the last row checking
            if target == matrix[row-1][k]:
                return True
        return False




        