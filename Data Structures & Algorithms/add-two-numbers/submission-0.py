class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        traverser1, traverser2 = l1, l2                        
        res = ListNode()
        res_traverser = res
        carry = 0
        while traverser1 and traverser2:
            total = carry + traverser1.val + traverser2.val          
            res_traverser.val = total % 10
            carry = total // 10                                     
            traverser1 = traverser1.next
            traverser2 = traverser2.next
            if traverser1 or traverser2 or carry:                
                res_traverser.next = ListNode()
                res_traverser = res_traverser.next

        while traverser1:
            res_traverser.val = (carry + traverser1.val) % 10
            carry = (carry + traverser1.val) // 10
            traverser1 = traverser1.next
            if traverser1 or carry:                             
                res_traverser.next = ListNode()
                res_traverser = res_traverser.next

        while traverser2:
            res_traverser.val = (carry + traverser2.val) % 10
            carry = (carry + traverser2.val) // 10                   
            traverser2 = traverser2.next
            if traverser2 or carry:                                 
                res_traverser.next = ListNode()
                res_traverser = res_traverser.next

        if carry:                                                  
            res_traverser.val = carry
        return res

