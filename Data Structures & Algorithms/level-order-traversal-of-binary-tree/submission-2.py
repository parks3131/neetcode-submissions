# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
                                                   #BFS
        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:                        #filters the null node
                    level.append(node.val)
                    q.append(node.left)         #no filer of nulls
                    q.append(node.right)
            if level:
                res.append(level)
        return res



