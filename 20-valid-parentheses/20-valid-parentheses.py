class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {  ")" : "(",    "}"  : "{",   "]"  : "[" }
         
        stack = []
    
        for c in s:
            if c in parenMap:
                if stack and parenMap[c] == stack[-1]:
                    stack.pop()
                else:
                    print("a")
                    return False
            else:
                stack.append(c)

        if not stack:
            return True 
            



    
        