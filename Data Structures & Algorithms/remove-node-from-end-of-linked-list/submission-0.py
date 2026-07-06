# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        prev = None
        while(first):
            temp = first.next
            first.next = prev
            prev = first
            first = temp

        new_head = prev
        curr = prev

        if n==1:
            new_head = new_head.next

        else:
            for i in range(1,n-1):
                curr = curr.next
            curr.next = curr.next.next
    
        first = None
        while(new_head):
            temp = new_head.next
            new_head.next = first
            first = new_head
            new_head = temp

        return first



            
