# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            
            kth = self.getKth(groupPrev, k)
            
            if not kth:
                break
            
            groupNext = kth.next
            
            pre,cur = kth.next,groupPrev.next
            
            while cur != groupNext:
                third = cur.next
                cur.next = pre
                pre = cur
                cur = third
            
            tmp  =  groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
            
            
    
    def getKth(self, curr, n):
        
        while curr and n:
            curr = curr.next
            n -= 1
        return curr
            
            
            

            
            
        
        
