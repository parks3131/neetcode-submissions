class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0], reverse = False)
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in range(len(intervals)):
            if end >= intervals[interval][0]:
                end = max(end, intervals[interval][1])
            else:
                res.append([start,end])
                start = intervals[interval][0]
                end = intervals[interval][1]
        if res and [start, end] == res[-1]:
            return res
        res.append([start,end])   
        return res
