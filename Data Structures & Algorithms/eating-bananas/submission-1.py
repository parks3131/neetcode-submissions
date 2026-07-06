class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        res = piles[-1]
        l, r = 1, piles[-1]
        while l<=r:
            k = (l+r)//2
            count = 0
            for i in range(len(piles)):
               count+= math.ceil(piles[i]/k)
            if count <= h:
                r = k-1
                res = min(res,k)
            else:
                l = k+1
        return res


