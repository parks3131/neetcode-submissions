class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #first lets find the target and then we have to find the firs and last
        #finding any target will be logn binary search 
        #should make the finding of the start and end using binary search
        #which makes that logn so as a whole we will get logn
        def searchLeft(target, right):
            l, r = 0, right
            while l < r:
                mid = l + (r - l)//2
                if nums[mid] != target:
                    l = mid + 1
                else:
                    r = mid
            return r

        def searchRight(target, left):
            l, r = left, len(nums) - 1
            while l < r:
                mid = l + (r - l + 1)//2
                if nums[mid] != target:
                    r = mid - 1
                else:
                    l = mid
            return l
    
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return [searchLeft(target, mid), searchRight(target, mid)] 
        return [-1, -1]