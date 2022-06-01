# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        following = head
        current = head 
        previous = None
        
        while current:
            following = following.next 
            current.next  =  previous
            previous = current 
            current  = following 
        return previous
        