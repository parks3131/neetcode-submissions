class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order = {}
        for i in range(len(nums)):
            if nums[i] in order:
                order[nums[i]]+=1
            else:
                order[nums[i]] = 1
        res = sorted(order.items(),key = lambda x:x[1],reverse = True)
        return [a for a,b in res[0:k]]