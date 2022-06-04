class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(n):
            if x == 0: return 0
            if n == 0: return 1
            
            tmp = n // 2
            res = dfs(tmp)
            res = res * res
            if n % 2 != 0:
                res *= x
            return res
        
        val = dfs(abs(n))
        return val if n >=0 else 1 /val
                
                
            

            

        
        
        
        
 
        