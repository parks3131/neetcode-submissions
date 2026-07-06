class Leaderboard:

    def __init__(self):
        self.hashmap = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hashmap:
            self.hashmap[playerId] = 0
        self.hashmap[playerId]+=score

    def top(self, K: int) -> int:
        minheap = []
        for score in self.hashmap.values():
            heapq.heappush(minheap, score)
            if len(minheap) > K:
                heapq.heappop(minheap)

        res = 0
        while minheap:
                res+=heapq.heappop(minheap)
        return res

    def reset(self, playerId: int) -> None:
        self.hashmap[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
