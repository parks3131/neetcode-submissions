class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Optimized Prefix method
        prefix_hash = defaultdict(int)
        prefix_hash[0]+=1
        prefix_sum = 0
        target, res = k, 0
        for i in range(0,len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum - target in prefix_hash:
                res+= prefix_hash[prefix_sum - target]
            prefix_hash[prefix_sum]+=1
        return res
