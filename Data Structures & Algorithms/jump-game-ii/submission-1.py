class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = res = 0
        maximum = 0
        while r < len(nums)-1:
            for r in range(l,r+1):
                maximum = max(r+nums[r],maximum)
            l=r+1
            r=maximum
            res+=1
        return res
            