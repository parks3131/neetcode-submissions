# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #so to find if cycle exist we gonna make the fast to meet slow
        if not head:
            return False
        slow, fast = head, head.next
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow == fast:
                return True
        return False
