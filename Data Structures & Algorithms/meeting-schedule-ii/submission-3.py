"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #arrang all intervals according to the starting time
        #we might use a minstack

        intervals.sort(key = lambda X:X.start, reverse = False)
        minheap = []
        maxdays = 0
        if not intervals:
            return 0
        heapq.heappush(minheap, intervals[0].end)
        for i in range(1, len(intervals)):
            if minheap[0] <= intervals[i].start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[i].end)
        return len(minheap)