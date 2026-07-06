# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iterator_1 = list1
        iterator_2 = list2

        res = ListNode()
        pointer = res
        
        while(iterator_1 and iterator_2):
            if iterator_1.val >= iterator_2.val:
                res.next = iterator_2
                iterator_2 = iterator_2.next
            else:
                res.next = iterator_1
                iterator_1 = iterator_1.next
            res = res.next

        res.next = iterator_1 if iterator_1 else iterator_2 
        
        return pointer.next



        