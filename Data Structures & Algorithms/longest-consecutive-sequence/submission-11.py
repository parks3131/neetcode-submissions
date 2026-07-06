class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #here we need the length of the consecutive numbers
        #so it is better to find whether the number which we select
        #is the start of the consecutive sequence because it is unnecessary 
        #to count the length of the other number of the same sequence for efficiency
        if not nums:
            return 0
        longest = 0
        for i in nums:
            if i-1 not in nums:
                length = 1
                while(i+length in nums):
                    length+=1
                longest = max(length,longest)
        return longest