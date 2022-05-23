class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        print(s)
        l , r = 0 , len(s) -1 
        vowels = "aeiouAEIOU"
        while l < r:
            if s[l] != s[r]: 
                if s[l] in vowels and s[r] in vowels:
                    s[l],s[r] = s[r],s[l]
                    l+=1
                    r-=1
                if s[l] not in vowels: l+=1
                if s[r] not in vowels: r-=1
                
            else:
                l+=1
                r-=1
        return "".join(s)
        