class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order = {}
        for i in nums:
            if i in order:
                order[i]+=1
            else:
                order[i] = 1
        res = sorted(order.items(),key = lambda x:x[1],reverse = True)
        return [a for a,b in res[0:k]]