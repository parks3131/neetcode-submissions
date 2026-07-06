# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeOne = head
        nodeTwo = head
        while(nodeTwo and nodeTwo.next):
            nodeOne = nodeOne.next
            nodeTwo = nodeTwo.next.next
            if nodeOne == nodeTwo:
                return True
        return False