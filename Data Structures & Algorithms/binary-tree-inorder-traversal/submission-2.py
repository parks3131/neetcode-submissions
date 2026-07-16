# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        #So we are saving the node values in an array and 
        #we will be using the recursion to address this problem
        #Recursion is a self defining function so we will first
        #define a function called inorde()
        def inorder(root):
            if not root:
                return     #we will dig deep until we wont see root with 
                            #no left or right node
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res