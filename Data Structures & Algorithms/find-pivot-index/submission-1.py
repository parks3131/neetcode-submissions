class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for i,pivot in enumerate(nums):
            rightSum-= pivot
            if leftSum == rightSum:
                return i
            leftSum+= pivot
        return -1
