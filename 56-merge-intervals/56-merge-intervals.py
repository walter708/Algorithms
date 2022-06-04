class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        slow = 0
        res = [intervals[slow]]
        for fast in range(1,   len(intervals)):              
            if (res[slow][1] >=  intervals[fast][0]) and (res[slow][1] <  intervals[fast][1]):
                res[slow] = [res[slow][0], intervals[fast][1]]
                
            elif (res[slow][1] <  intervals[fast][0]) and (res[slow][1] <  intervals[fast][1]): 
                res.append(intervals[fast])
                slow += 1
        return res

                