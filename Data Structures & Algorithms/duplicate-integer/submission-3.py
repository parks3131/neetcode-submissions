class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i]+=1
            if hashmap[i] > 1:
                return True
        return False