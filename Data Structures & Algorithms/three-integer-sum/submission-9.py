class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                num = nums[i]
                target = nums[l]+num+nums[r]
                if target < 0:
                    l+=1
                elif target > 0:
                    r-=1
                else:
                    res.append([nums[l],num,nums[r]])
                    l+=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
        
        return res

