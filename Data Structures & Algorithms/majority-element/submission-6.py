class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = nums[0]
        for i in nums:
            if curr == i:
                count+=1
            else:
                count-=1
            if count < 0:
                curr = i
        return curr
