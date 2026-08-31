class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for curr in range(len(nums)):
            if nums[curr] > 0:
                break
            if curr != 0 and nums[curr] == nums[curr - 1]:
                continue
            left = curr + 1
            right = len(nums) - 1
            while left < right:
                target = nums[left] + nums[curr] + nums[right]
                if target == 0:
                    res.append([nums[curr], nums[left], nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
                else:
                    if target > 0:
                        right-=1
                    else:
                        left+=1
        return res
                

