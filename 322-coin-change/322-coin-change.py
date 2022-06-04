class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount, memo):
            if amount == 0:
                return [] 
            if amount < 0:
                return -1 
            if amount in memo:
                return memo[amount]
            
            miniCoin = -1
            
            
            for coin in coins:
                rmd = amount - coin
                
                value = dfs(rmd, memo)
                
                if value != -1:
                    comb = [i for i in value]
                    comb.append(coin)
                    
                    if  miniCoin == -1 or len(comb) < len(miniCoin):
                        miniCoin = comb
                        
            memo[amount] = miniCoin
            
            return memo[amount]
                        

                    

        
        val = dfs(amount, memo)
        return val if val == - 1 else len(val)
                
            
        
            
            
            
        