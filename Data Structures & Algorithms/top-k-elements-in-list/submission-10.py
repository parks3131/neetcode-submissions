class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] +=1
            else:
                hash_map[i] = 1
        sort = sorted(hash_map.items(),key = lambda X:X[1],reverse = True)
        return [a for a,b in sort[:k]]
        