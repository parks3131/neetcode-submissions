"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #here we are gonna sort it according to the finishing time and 
        #compare the finishing time with the next starting time

        sort = sorted(intervals, key = lambda x: x.end, reverse = False)
        for i in range(len(sort)-1):
            if sort[i].end > sort[i+1].start:
                return False
        return True

