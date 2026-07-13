class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0], reverse = False)
        start, end = intervals[0][0], intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            if end <= intervals[i][0]:
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                if end > intervals[i][1]:           # The key logic eliminate the end with highest value
                    end = intervals[i][1]
                    start = intervals[i][0]
                count+= 1
        return count

                    