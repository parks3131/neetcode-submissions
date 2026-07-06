class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #arrange according to the ending time asc
        #update the end element for each iteration in list where end element >= intervals[i][0]
        #update the front element only when end element < intervals[i][0] then append it into a res

        
        res = []
        intervals = sorted(intervals, key = lambda x:x[0], reverse = False)
        

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1,len(intervals)):
            if end >= intervals[i][0]:
                end = max(end,intervals[i][1])
                
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        if [start,end] not in res:
            res.append([start,end])
        return res
