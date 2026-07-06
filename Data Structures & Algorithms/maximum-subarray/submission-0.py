class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curMax = 0
        maxNumber = float("-inf")

        for x in nums:
            curMax = curMax + x

            if curMax < 0:
                maxNumber = max(maxNumber, curMax)
                curMax = 0
            else:
                maxi = max(maxi, curMax)

        return maxNumber if maxi < 0 else maxi
