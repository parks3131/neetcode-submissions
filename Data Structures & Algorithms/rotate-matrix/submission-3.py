class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0])-1 #note it is a square matrix
        while l<r:
            top, bottom = l, r
            for i in range(r-l):

                topleft = matrix[top][l+i]

                #topleft will be replaced by bottom left
                matrix[top][l+i] = matrix[bottom-i][l]
                #bottom left will be replaced by bottom right
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #bottom right will be replaced by top right
                matrix[bottom][r-i] = matrix[top+i][r]
                #top right will be replaced by top left
                matrix[top+i][r] = topleft

            l+=1# we are adding and sub
            r-=1# to move into next inner matrix
