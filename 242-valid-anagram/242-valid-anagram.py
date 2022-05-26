class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countDic = {}
        
        for i in s:
            if i not in countDic:
                countDic[i] = 1
            else:
                countDic[i]  += 1
        for j in t:
            if j not in countDic:
                return False
            countDic[j]-=1
        
        for val in countDic.values():
            if val != 0:
                return False
        return True 
