class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid) , len(grid[0])
        count = 0
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0":continue
                if self.explore(grid , i , j , visit):
                    count+=1
        return count
    def explore(self, grid, i , j , visit):
        rowBound = i >= 0 and i < len(grid)
        colBound = j >= 0 and j < len(grid[0])
        
        if not rowBound:return False
        if not colBound:return False
        pos = (i , j)
        if pos in visit:return False
        visit.add(pos)
        if grid[i][j] == "0":return False
        
        self.explore( grid, i+1 , j , visit)
        self.explore( grid, i-1 , j , visit)
        self.explore( grid, i , j+1 , visit)
        self.explore( grid, i , j-1 , visit)
        return True 
        
        
        
        