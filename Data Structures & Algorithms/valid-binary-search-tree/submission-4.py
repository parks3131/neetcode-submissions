# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        list_ascending = []
        def inorder(root:Optional[TreeNode]):
            if not root:
                return  
            left = inorder(root.left)
            list_ascending.append(root.val)
            right = inorder(root.right)
        
        inorder(root)

        return all(list_ascending[i]<list_ascending[i+1] for i in range(len(list_ascending)-1))

            

        
         
        
        