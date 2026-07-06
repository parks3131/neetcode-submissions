"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
            #check any are in the range of any others
            #structure it first of all, but by which ?
            #we are gonna structure in by start time in ascending
            #the only thing we will be updating is endtime
            #endtime <= nextstart: then end = nextend
            #endtime > nextstart: then we will return False
            if not intervals:
                return True
            intervals.sort(key = lambda X:X.start, reverse = False)
            end = intervals[0].end
            for i in range(1,len(intervals)):
                nextstart = intervals[i].start
                if end <= nextstart:
                    end = intervals[i].end
                else:
                    return False
            return True
