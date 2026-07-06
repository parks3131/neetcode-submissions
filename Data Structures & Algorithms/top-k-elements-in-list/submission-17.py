class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #now count is a dictionary of the frequency
        #we want to place the numbers on a list where the indices denotes
        #no of times the number occurs here is the catch a particular index
        #can have more than one number, so the numbers will be stored in lists attached
        #to a specific index
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        res = []

        for n,c in count.items():
            freq[c].append(n)
        
        for i in range(len(nums),0,-1):
            for _ in freq[i]:
                res.append(_)
                if len(res) == k:
                    return res
        
