class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)

        longest = 0
        length = 1

        for i in nums:
            if i-1 not in nums:
                length = 1
                while(i+length in nums):
                    length+=1
                longest = max(longest,length)
        return longest
            

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    
    
            