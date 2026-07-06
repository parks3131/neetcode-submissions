class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #arrange it according to the ending time in ascending order
        #we need a res to append all non over lapping
        #we need to use a for loop to traverse through out the intervals
        #return the res probably we need a condition at last for adding the 
        #last set to the list

        intervals.sort(key = lambda x:x[0], reverse = False)
        res = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1,len(intervals),1):
            if end >= intervals[i][0]:
                end = max(end,intervals[i][1])
            else:
                res.append([start,end])
                start, end = intervals[i][0], intervals[i][1]
        if [start,end] not in res:
            res.append([start,end])
        return res
            
            

        