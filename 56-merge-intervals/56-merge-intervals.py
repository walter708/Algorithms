class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        slow = 0
        
        for fast in range(1 , len(intervals)):
            if result[slow][1] < intervals[fast][0]:
                result.append(intervals[fast])
                slow+=1
            elif (result[slow][1] > intervals[fast][0]) and (result[slow][1] > 
            intervals[fast][1]):
                continue
            elif ( result[slow][1] >= intervals[fast][0] ) and (result[slow][1] < intervals[fast]               [1]):
                result[slow] = [result[slow][0] , intervals[fast][1]]
        return result
                