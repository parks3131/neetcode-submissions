class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float("-inf")
        Sum = 0
        for num in nums:
            Sum+=num
            maximum = max(maximum, Sum) 
            if Sum < 0:
                Sum = 0
        return maximum
            
