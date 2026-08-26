# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        #Bainstorming
        #So i need a function to detect the the same tree
        #then recursively ill go and check the nodes and know if it returns true its true
        #if not after traversing the whole tree we know it is false

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, treeOne, treeTwo):
        if not treeOne and not treeTwo:
            return True
        if treeOne and treeTwo and treeOne.val == treeTwo.val:
            return self.sameTree(treeOne.left, treeTwo.left) and self.sameTree(treeOne.right, treeTwo.right)
        return False

        