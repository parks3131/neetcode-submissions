class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #arrange in ascending order of start time
        #we gonna compare the 
        #start = 1 and endtime = 3
        #endtime >= next start time then max(endtime,nextendtime)
        #endtime < startime starttime = startnext and endtime = endtimenext

        intervals.sort(key = lambda X:X[0], reverse = False)

        start = intervals[0][0]
        end = intervals[0][1]
        res = []

        for i in range(1, len(intervals)):
            nextstart = intervals[i][0]
            nextend = intervals[i][1]

            if end >= nextstart:
                end = max(end, nextend)
            else:
                res.append([start, end])
                start, end = nextstart, nextend
        if res:
            if [start, end] != res[-1]:
                res.append([start, end])
        else:
            res.append([start, end])
        return res