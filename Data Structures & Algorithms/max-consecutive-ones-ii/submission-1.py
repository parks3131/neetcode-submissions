class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sumArray = [0]*len(nums)
        count = 0
        if 0 not in nums:
            return sum(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                sumArray[i] = count
                count = 0
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                count+=1
            else:
                sumArray[i]+= count + 1 #+1 including that 0 as 1
                count = 0
        return max(sumArray)
        
        