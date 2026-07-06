# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head) # we might need to remove the head too
        left = dummyNode
        right = head

        for i in range(n):
            right = right.next
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummyNode.next
        


