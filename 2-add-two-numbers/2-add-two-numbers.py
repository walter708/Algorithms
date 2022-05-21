# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add(head1 , head2 , carry = 0):
            if head1 == None and head2 == None and carry==0:
                return None
            
            val1 = 0 if head1 == None else head1.val
            val2 = 0 if head2 == None else head2.val
            
            res = val1 + val2 + carry
            nextCarry = 0 if res <=  9 else 1
            digit = res % 10
            next1 = None if head1 == None else head1.next
            next2 = None if head2 == None else head2.next
            resultNode = ListNode(digit)
            resultNode.next = add(next1 , next2 , nextCarry)
            return resultNode
        return add(l1 , l2)
            
            

            
            

        
        

        
        