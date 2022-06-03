# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA 
        l2 = headB
        
        c1 = 0
        c2 = 0
        
        while l1:
            l1 = l1.next
            c1+=1

        while l2:
            l2 = l2.next
            c2+=1 
            
        l1 = headA 
        l2 = headB   
        
        if c1 > c2:
            diff = c1 - c2
            while diff:
                l1 = l1.next
                diff-=1
        elif c2 > c1:
            diff2 = c2 - c1
            while diff2:
                l2 = l2.next
                diff2-=1 
                
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
            
        return l1
        
        
        
        
        
        