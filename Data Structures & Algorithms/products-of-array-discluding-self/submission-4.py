class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = 1
        left = [0]*len(nums)
        rightProduct = 1
        for i in range(len(nums)):
            left[i] = leftProduct
            leftProduct*=nums[i]
        for i in range(len(nums)-1, -1, -1):
            left[i] = rightProduct*left[i]
            rightProduct*=nums[i]
        return left