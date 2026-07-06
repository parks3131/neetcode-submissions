class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda X:X[0], reverse = False)
        available = [i for i in range(n)]
        used = [] #(endTime, roomno)
        count = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                endThatWeDontUse, room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                #we should alter the endtime
                (endTime, room) = heapq.heappop(used)
                end = endTime + (end - start)
                heapq.heappush(available, room)
            
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room]+=1
        
        return count.index(max(count))