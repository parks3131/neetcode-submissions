class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        Sum = 0
        for i in range(len(nums)):
            Sum+= nums[i]
            res = max(res,Sum)
            if Sum < 0:
                Sum = 0
        return res