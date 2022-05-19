# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or  not head.next:
            return head 
        left = head
        right = self.getMiddle(head)
        tmp = right.next
        right.next = None 
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)
        return  self.merge(left, right)
    
    def getMiddle(self, head:  Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head , head.next
        
        while fast and  fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left , right)-> Optional[ListNode]:
        tail = dummy = ListNode()
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            elif right.val <= left.val:
                tail.next = right
                right = right.next
            tail  = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next

            
        
        