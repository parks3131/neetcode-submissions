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
        room = []
        heapq.heappush(room, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= room[0]:
                heapq.heappop(room)
            heapq.heappush(room, intervals[i].end)
        return len(room)

        