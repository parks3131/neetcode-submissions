class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #so make it ascending according to start time and remove prioritizing lengthy end time
        intervals.sort(key = lambda x:x[0], reverse = False)
        start = intervals[0][0]
        end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                res+=1
                end = min(end, intervals[i][1])
        return res

                    