class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if ord(char) < 97 or ord(char) > 122:
                if ord(char) >= 48 and ord(char) <= 57:
                    continue
                s = s.replace(char,"")

                
                
        print(s)                
        l, r = 0 , len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False 
            
            l+=1
            r-=1
        return True
                
            