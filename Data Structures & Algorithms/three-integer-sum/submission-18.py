class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for cur in range(len(nums)):
            if nums[cur] > 0: # early quit we know there is no way the sum will be zero
                break
            if cur !=0 and nums[cur - 1] == nums[cur]:
                continue
            l, r = cur + 1, len(nums) - 1
            while l < r:
                Sum = nums[cur] + nums[l] + nums[r]
                if Sum == 0:
                    res.append([nums[cur], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l - 1] == nums[l]:
                        l+=1
                elif Sum > 0:
                    r-= 1
                else:
                    l+=1
        return res
