"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start, reverse = False)
        minheap = []
        heapq.heappush(minheap,intervals[0].end)

        for i in range(1,len(intervals)):
            if minheap[0] <= intervals[i].start:
                heapq.heappush(minheap,intervals[i].end)
                heapq.heappop(minheap)
            else:
                heapq.heappush(minheap,intervals[i].end)
        return len(minheap)
