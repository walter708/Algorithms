class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupCount = {}
        res = []
        for s in strs:
            tmp = sorted(s)
            tmp = "".join(tmp)
            if tmp not in groupCount:
                groupCount[tmp] = []
            groupCount[tmp].append(s)
        
        
        for key , value in groupCount.items():
            res.append(value)
            
        return res
                

         