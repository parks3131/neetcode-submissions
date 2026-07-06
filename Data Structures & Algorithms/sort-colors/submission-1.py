class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, curr, r = 0, 0, len(nums)-1
        while(curr <= r):
            if nums[curr] == 1:
                curr+=1
            elif nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                l+=1
                curr+=1
            else:
                nums[r], nums[curr] = nums[curr], nums[r]
                r-=1
            