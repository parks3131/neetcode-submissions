class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        count = defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)

        for i,num in count.items():
            if len(num)>1:
                diff = float("inf")
                for j in range(len(num)-1):
                    diff = min(diff,abs(num[j]-num[j+1]))
                if diff <= k:
                    return True
                else:
                    return False                   
        return False