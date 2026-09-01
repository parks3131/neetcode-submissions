class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        Sum, res = 0, 0
        for i in range(len(nums)):
            Sum+= nums[i]
            if Sum - k in hashmap:
                res+= hashmap[Sum - k]
            hashmap[Sum]+=1
        return res

            

