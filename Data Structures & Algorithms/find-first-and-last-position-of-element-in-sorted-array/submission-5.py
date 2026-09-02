class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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