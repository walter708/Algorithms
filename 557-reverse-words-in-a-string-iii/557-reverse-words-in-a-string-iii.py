class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split(" ")
        res = ""
        for i in range(len(splited)):
            res+="".join(splited[i][::-1] + " ")
            
        val = res.strip()
        return val
        