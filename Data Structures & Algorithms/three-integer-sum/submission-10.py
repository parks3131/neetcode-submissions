class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #-4 -1 -1 0 1 2 
        #    c  l     r
        #0
        for curr in range(len(nums)):
            if curr > 0 and nums[curr - 1] == nums[curr]:
                continue
            l, r = curr + 1, len(nums) - 1
            while l < r:
                threeSum = nums[curr] + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([nums[curr], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l - 1] == nums[l]:
                        l+=1
        return res
                

            