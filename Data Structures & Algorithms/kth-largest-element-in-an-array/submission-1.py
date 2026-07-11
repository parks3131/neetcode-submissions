class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        toPop = len(nums) - k 
        #2 5 8 9 18 57
        for i in range(toPop):
            heapq.heappop(nums)
        return heapq.heappop(nums)
