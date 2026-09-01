class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0], reverse = False)
        res = []

        start, end = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            if end < intervals[i][0]:
                res.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        if not res:
            return [[start, end]]
        if res and [start, end] != res[-1]:
            res.append([start, end])
            return res