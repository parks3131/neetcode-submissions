# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        startptr = head
        count = 0
        if not head or not head.next:
            return head 
        while(ptr):
            count+=1
            ptr = ptr.next
        k = k % count
        ptr = head
        for i in range(k): 
            ptr = ptr.next
        while(ptr.next):
            startptr = startptr.next
            ptr = ptr.next

        ptr.next = head
        head = startptr.next
        startptr.next = None
        
        return head
        
        
