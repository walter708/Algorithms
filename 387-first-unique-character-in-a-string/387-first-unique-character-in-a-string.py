class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = {}
        
        for i in s:
            if i not in countMap:
                countMap[i] = 0
            countMap[i]+=1
            
        for index , value in enumerate(s):
            if countMap[value] == 1:
                return index
        return -1
        

                
            
        