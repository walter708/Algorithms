class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = {}
        
        for cha in s:
            countMap[cha] = 1 + countMap.get(cha , 0)
        
        for i in range(len(s)):
            if countMap[s[i]] == 1:
                return i
        return -1
            

        

                
            
        