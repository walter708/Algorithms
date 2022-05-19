# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #            -inf < 5 < inf  - > true
        #                 /   \
        # -inf  3 < 5 -> true    5 < 7 < inf - > true 
        #                             /        \
        #                  5 < 4 < 7 -> False   7 < 8 < inf - > true 
        
        def valid(node , left , right):
            if not node:
                return True 
            if not (node.val < right  and  node.val > left):
                return False
            return (valid(node.left , left , node.val) and
                   valid(node.right , node.val , right))
        return valid(root , float('-inf') , float('inf'))
            
        

        
        