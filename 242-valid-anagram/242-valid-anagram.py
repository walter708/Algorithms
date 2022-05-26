class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        countOne = {}
        countTwo = {}
        
        for i in range(len(s)):
            if(s[i] not in countOne):
                countOne[s[i]] = 0
            countOne[s[i]] += 1
         
        for j in range(len(t)):
            if(t[j] not in countTwo):
                countTwo[t[j]] = 0
                
            countTwo[t[j]] += 1
            
        for key in countOne.keys():
            
            if countOne[key] != countTwo.get(key , 0):
                return False
        return True