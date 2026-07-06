class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxpos = nums[0]
        maxneg = float("-inf")
        currSum = 0

        for i in nums:
            currSum+=i
            if currSum<0:
                maxneg = max(maxneg,currSum)
                currSum=0
            else:
                maxpos = max(maxpos,currSum)
        return maxneg if maxpos<0 else maxpos
