class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum, res = 0, 0
        hashmap = defaultdict(int)
        hashmap[0]+=1
        for num in nums:
            currSum+=num
            diff = currSum - k
        
            if diff in hashmap:
                res+=hashmap[diff]
            hashmap[currSum]+=1
        return res

                