class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if we are getting only -ve numbers we are not adding it just wanna return the 
        #smallest negative number
        #else we will add it the sub array until sum > 0 if it goes below 0 there is 
        #no point in doing maximum sum of subarray because regardless it is gonna be less than
        #some part of subarray

        Sum = 0
        res = float("-inf")
        for i in nums:
            Sum+= i
            res = max(res, Sum)
            if Sum < 0:
               Sum = 0 
        return res
            
