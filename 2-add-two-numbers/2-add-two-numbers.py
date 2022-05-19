# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0 
        dummy = ListNode()
        tail = dummy 
        while l1 and l2:
            res = l1.val + l2.val  #  9 + 9 = 18 
            res = res + remainder  # 18 + 0 = 18 
            remainder = 0      
            # if res >= 10:  # 18 >  #  
            #     l1.val = res % 10  # 8 
            #     tail.next = l1     #  8 
            #     remainder = res // 10  # 1
            # else:    
            #     l1.val = res
            #     tail.next = l1
            remainder = self.refactor(res, l1 , tail, remainder)
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        while l1:
            res = l1.val + remainder 
            remainder = 0 
            print(res)
            # if res >= 10:
            #     l1.val = res % 10
            #     tail.next = l1
            #     remainder = res // 10
            # else:
            #     l1.val = res
            #     tail.next = l1
            remainder =self.refactor(res, l1 , tail, remainder)
            tail = tail.next
            l1 = l1.next
        while l2:
            res = l2.val + remainder # 9 + 
            remainder = 0 
            # if res >= 10:
            #     l2.val = res % 10
            #     tail.next = l2
            #     remainder = res // 10
            # else:
            #     l2.val = res
            #     tail.next = l2
            remainder =self.refactor(res, l2 , tail, remainder)
            tail = tail.next
            l2 = l2.next
        if remainder:
            lastNode = ListNode(remainder)
            tail.next = lastNode
        return dummy.next
    # 2 4
            
    def refactor(self, res, head , tail, remainder):
        if res >= 10:  # 18 >  #  
            head.val = res % 10  # 8 
            tail.next = head     #  8 
            remainder = res // 10  # 1
        else:    
            head.val = res
            tail.next = head
        return remainder
        
        
        # 2 -> 4 -> 3 ==> 342
        # 5 -> 6 -> 4 ==> 465
        # 7    10 % 10 = 0 10// 10 = 1 
        # remainder = 1 
        #           7 
        
        # 2 -> 4 -> 3 -> 6 list 
        # 5 -> 6 -> 4
        
        