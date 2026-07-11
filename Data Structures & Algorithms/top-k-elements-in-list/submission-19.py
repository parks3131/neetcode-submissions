from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)  # {value: frequency}
        heap = []
        for value, freq in counts.items():
            heapq.heappush(heap, (-freq, value))
        return [heapq.heappop(heap)[1] for _ in range(k)]