class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, Sum = float("-inf"), 0
        for i in nums:
            Sum+=i
            res = max(res,Sum)
            if Sum < 0:            #-2 7 ans 7 
                Sum = 0            #-2 -9 -8 ans 8 
        return res                 #closely watch how sum and res helps
