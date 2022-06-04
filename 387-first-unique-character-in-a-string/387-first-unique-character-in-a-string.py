class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = {}
        
        for cha in s:
            countMap[cha] = 1 + countMap.get(cha, 0)
        
        for index, cha in enumerate(s):
            if countMap[cha] == 1:
                return index
        return  - 1

            

        

                
            
        