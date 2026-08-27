# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #So we need a max to store the sum and when advancing each level up we will
        #take themax of left or right.
        Max = 0
        def findDiameter(root):
            nonlocal Max
            if not root:
                return 0
            left = findDiameter(root.left)
            right = findDiameter(root.right)
            Max = max(Max, left + right)
            return 1 + max(left, right)
        findDiameter(root)
        return Max