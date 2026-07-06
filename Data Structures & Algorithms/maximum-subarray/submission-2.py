class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, Sum = float("-inf"), 0
        for i in nums:
            Sum+=i
            res = max(res,Sum)
            if Sum < 0:
                Sum = 0
        return res
