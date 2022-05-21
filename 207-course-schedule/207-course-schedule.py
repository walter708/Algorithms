class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        crsPreq = {i :[] for i in range(numCourses)}
        for crs , preq in prerequisites:
            crsPreq[crs].append(preq)
            
        def dfs(crs):
            if crsPreq[crs] == []: return True
            if crs in visit:return False
            visit.add(crs)
            
            for preq in crsPreq[crs]:
                if not dfs(preq):return False
            
            visit.remove(crs)
            crsPreq[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True 
        