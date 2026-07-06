# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traversal(curr)-> List[Optional[int]]:
            if not curr:
                return [None]
            left = traversal(curr.left)
            right = traversal(curr.right)

            return left + right + [curr.val]
        return True if traversal(p) == traversal(q) else False 
        
                
