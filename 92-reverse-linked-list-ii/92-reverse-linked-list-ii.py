# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n = left 
        m = right
        curr, pre = head, None
        
        while n > 1:
            pre = curr
            curr = curr.next
            n, m = n - 1 , m - 1
            
        con, tail = pre, curr
        
        while m:
            third = curr.next 
            curr.next = pre
            pre = curr
            curr = third
            m -=1
            
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = curr
        return head
        
            
            
            
            
        

    
        
        
        
        