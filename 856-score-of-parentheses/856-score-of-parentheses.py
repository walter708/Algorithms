class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        
        for i in s:
            if i == ")":
                val = stack.pop()
                stack[-1] += max(2 * val , 1) 
            if i == "(":
                stack.append(0)
                
        return stack[0]
            

        

        