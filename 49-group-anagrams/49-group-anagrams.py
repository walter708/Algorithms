class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {} 
        
        for s in strs:
            
            array = [0] * 26
            
            for l in s:
                array[ord(l) - ord('a')] +=1
                
            if tuple(array) not in hashMap:
                hashMap[tuple(array)] = []
                
            hashMap[tuple(array)].append(s)
            
        return hashMap.values()

                

         