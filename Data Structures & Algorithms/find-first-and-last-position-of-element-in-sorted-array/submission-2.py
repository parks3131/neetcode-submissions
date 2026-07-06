class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left(nums,target):
            l, r, lmid = 0, len(nums)-1, -1
            while l<=r :
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[mid] == target:
                        lmid = mid
                    r = mid-1
            return lmid

        def right(nums,target):
            l, r, rmid = 0, len(nums)-1, -1
            while l<=r :
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid] == target:
                        rmid = mid
                    l = mid + 1
            return rmid
        
        l = left(nums,target)
        r = right(nums, target)
        if left == -1:
            return [-1,-1]
        else:
            return [l,r]


            


