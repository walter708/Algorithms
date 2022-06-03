# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0 , head)
        groupPrev = dummy 
        
        while True:
            kth = self.getKth(groupPrev, k)
            
            if not kth:
                break
                
            groupNext = kth.next
            
            prev, curr = kth.next , groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev 
                prev = curr
                curr = tmp
            
            tm = groupPrev.next
            groupPrev.next = kth
            groupPrev = tm
            
        return dummy.next
            
            
    def getKth(self, curr, val):
        while curr and val > 0:
            curr = curr.next
            val-=1
        return curr