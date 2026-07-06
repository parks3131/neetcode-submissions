# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #First traverse the whole list to know the no of elements
        #then break it into half
        #reverse the second half
        #then arrange it accordingly
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        while head and prev:
            temp1, temp2 = head.next, prev.next
            head.next, prev.next = prev, temp1
            head, prev =temp1, temp2
           
            




