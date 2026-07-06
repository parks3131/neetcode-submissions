class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            RightSum = totalSum - nums[i] -leftSum
            if RightSum == leftSum:
                return i
            leftSum += nums[i]
        return -1