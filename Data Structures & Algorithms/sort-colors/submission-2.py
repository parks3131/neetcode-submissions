class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r, curr= 0, len(nums)-1, 0
        while curr <= r:
            if nums[curr] == 1:
                curr+=1
            elif nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l+=1
                curr+=1
            else:
                nums[curr], nums[r] = nums[r], nums[curr]
                r-=1

        