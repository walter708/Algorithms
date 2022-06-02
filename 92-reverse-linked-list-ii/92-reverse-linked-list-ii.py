# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        l, r, stop = head, head, False
        
        def recurseAndReverse(r, left, right):
            nonlocal l, stop
            
            if right == 1:
                return 
            
            r = r.next
            
            if left > 1:
                l = l.next
                
            recurseAndReverse(r, left - 1, right - 1)
            
            if r == l or r.next == l:
                stop = True
            
            if not stop:
                l.val , r.val = r.val , l.val
                
                l = l.next
        recurseAndReverse(r, left , right)
        return head
        
        
        