# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        leftprev = dummyNode
        leftNode, rightNode = head, head

        for i in range(right - left):
            rightNode = rightNode.next
        
        for i in range(left - 1):
            leftprev = leftprev.next
            leftNode, rightNode = leftNode.next, rightNode.next
        end = rightNode.next

        prev = None
        while leftNode != end:
            temp = leftNode.next
            leftNode.next = prev
            prev = leftNode
            leftNode = temp
        leftprev.next.next = end
        leftprev.next = prev
        return dummyNode.next