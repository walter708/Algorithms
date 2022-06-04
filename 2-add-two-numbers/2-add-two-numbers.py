# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                tail.next = l1
                tail = tail.next
            elif l2:
                tail.next = l2
                tail = tail.next
            else:
                tail.next = ListNode()
                tail = tail.next
                
            # print(dummy.next)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            total = val1 + val2 + carry
            digit = total % 10 
            carry = total // 10
            tail.val = digit

            
        return dummy.next
            
            
            


            
            

            
            

        
        

        
        