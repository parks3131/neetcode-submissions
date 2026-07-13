class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        start = newInterval[0]
        end = newInterval[1]
        res = []

        while i < len(intervals):
            if intervals[i][1] < start:
                res.append(intervals[i])
                i+=1
            else:
                break

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i+=1
        res.append([start, end])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
                
