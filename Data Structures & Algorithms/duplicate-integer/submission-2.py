class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i,num in count.items():
            if num>1:
                return True
        return False