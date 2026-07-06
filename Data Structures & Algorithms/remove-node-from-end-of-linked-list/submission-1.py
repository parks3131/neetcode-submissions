# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_Node = ListNode(0,head)
        #we are inserting a node before head to meet the offset difference
        #between Left and Right
        left = dummy_Node
        right = head
        while(n>0 and right):
            right = right.next
            n-=1

        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy_Node.next




            
