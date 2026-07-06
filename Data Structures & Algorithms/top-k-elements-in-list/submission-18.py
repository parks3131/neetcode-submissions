class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        hashmap = defaultdict(list)
        res = []

        for n,c in count.items():
            hashmap[c].append(n)
            
        for i in range(len(nums), 0, -1):
            for _ in hashmap[i]:
                res.append(_)
            if len(res) == k:
                return res