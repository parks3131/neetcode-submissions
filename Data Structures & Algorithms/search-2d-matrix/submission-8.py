class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        column = len(matrix)
        
        if column == 1:
            return True if target in matrix[0] else False
        i = 1
        while(i < column):
            if target <= matrix[i][0]:
                return True if target in matrix[i-1] or target == matrix[i][0] else False
            i+=1
        
        for k in range(row):  
            if target == matrix[column-1][k]:
                return True
        return False




        