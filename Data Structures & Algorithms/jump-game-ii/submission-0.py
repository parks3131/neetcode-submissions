class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = res = 0
        farthest = 0
        while r < len(nums)-1:
            for r in range(l,r+1):
                farthest = max(r+nums[r],farthest)
            l=r+1
            r=farthest
            res+=1
        return res
            