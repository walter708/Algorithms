class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        MAX = float('inf')
        
        dp = [0] + ([MAX] * amount)
        
        for  i in range(1, (amount + 1)):
            dp[i] = min([dp[i - c] if (i - c) >=0 else MAX for c in coins]) +  1
        
        if dp[-1] == MAX:
            return  - 1
        else:
            return dp[-1]

                
            
        
            
            
            
        