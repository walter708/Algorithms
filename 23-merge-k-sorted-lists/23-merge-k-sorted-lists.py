# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)  == 1:return lists[0]
        if len(lists) == 0:return None
        
        res = self.merger(lists[0] , lists[1])
        
        if len(lists) == 2: return res
        
        for i in range(2 , len(lists)):
            res = self.merger(res , lists[i])
        return res
            
        
    def merger(self, l1 , l2):
        tail = dummy = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
            
        