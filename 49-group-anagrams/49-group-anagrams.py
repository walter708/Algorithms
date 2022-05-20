class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countAnagram = {}
        res = []
        for i in strs:
            tmp = sorted(i)
            tmp = "".join(tmp)
            if tmp not in countAnagram:
                countAnagram[tmp] = []
            countAnagram[tmp].append(i)
        for key , val in countAnagram.items():
            res.append(val)
        return res
         