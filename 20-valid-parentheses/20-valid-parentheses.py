class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {"}" : "{" , "]" : "[" , ")" : "("}
        stack =[]
        
        for char in s:
            if char in charMap:
                if stack and charMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return True if len(stack) == 0 else False 



    
        