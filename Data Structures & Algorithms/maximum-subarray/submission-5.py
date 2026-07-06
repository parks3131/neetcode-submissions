class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        Sum = nums[0]
        for i in range(1,len(nums)):
            res = max(res,Sum)
            if Sum < 0:
                Sum = 0
            Sum+=nums[i]
        return max(res,Sum)