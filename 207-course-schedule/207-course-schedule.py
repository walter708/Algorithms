class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        courseMap = {n:[] for n in range(numCourses)}
        
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)
        
        def dfs(crs):
            if courseMap[crs] == []:
                return True
            if crs in visit:
                return False
            visit.add(crs)
            
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
                
            visit.remove(crs)
            courseMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                
        