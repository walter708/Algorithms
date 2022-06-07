"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []
        while stack:
            it = stack.pop()
            if it:
                res.append(it.val)  
                for child in it.children:
                    stack.append(child)
        
        res = res[::-1]
        return res
        