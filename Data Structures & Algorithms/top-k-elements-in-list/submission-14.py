class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = sorted(count.items(), key = lambda x:x[1], reverse = True )
        return [a for a,b in res[0:k]]