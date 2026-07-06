class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
            else:
                length = max(length,count)
                count=0
        length = max(length,count)
        return length

