class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 1
        length = 0
        count = 0
        for i in nums:
            if curr == i:
                count+=1
            else:
                length = max(length,count)
                count=0
        length = max(length,count)
        return length

