class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()        
        res = piles[-1]
        l, r = 1, piles[-1] # chances of k from 1 to max(Piles)
        while l <= r:
            k = l + (r - l)//2
            hours = 0
            for i in piles:
                hours+=math.ceil(i/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res