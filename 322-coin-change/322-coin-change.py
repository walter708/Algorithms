class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 1 and amount == 0:
            return 0
        memo = {} 
        def dfs(coins, amount, memo):
            if amount in memo:return memo[amount]
            if amount == 0:return 0
            if amount < 0 :return -1
            
            mini = float("inf")
            for i in coins:
                remainder = amount - i
                value = dfs(coins , remainder , memo)
                if value >= 0:
                    mini = min(value + 1 , mini)
            memo[amount] = mini
            return memo[amount]
        
        val = dfs(coins , amount , memo)            
        return val if val != float('inf') else -1
    
            
                
                
            
        
        