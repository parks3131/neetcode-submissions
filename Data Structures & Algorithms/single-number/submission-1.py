class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0       # n ^ 0 = n that is why we are starting with 0
        for i in nums:
            res = i ^ res
        return res