# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def height_calculate(curr):
            if not curr:
                return 0
            left = height_calculate(curr.left)
            right = height_calculate(curr.right) 

            self.result = max(self.result,left+right)

            return 1+ max(left,right)
        height_calculate(root)
        return self.result

            
    
        