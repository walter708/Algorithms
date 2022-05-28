class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
          
        sCount = {}
        pCount = {}
        res = []
        if len(p) > len(s):
            return []
        
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i] , 0)
            sCount[s[i]] = 1 + sCount.get(s[i] , 0)
        
        res = [0] if pCount == sCount else [] 
        
        l = 0
        
        for i in range(len(p) , len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i] , 0)
            sCount[s[l]] -=1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l+=1
            
            if pCount == sCount:
                res.append(l)
                
        return res
            
        

         
            

            
        
             
        
        