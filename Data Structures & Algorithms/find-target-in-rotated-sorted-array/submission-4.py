class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first figure out the starting point index
        #then binary search the target in the restected half

        def binarySearch(l, r):
            while l <= r:
                mid = l + (r - l)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        pivot = l
 
        if target == nums[pivot]:
            return pivot
        elif nums[pivot] < target and nums[-1] >= target:
            return binarySearch(pivot, len(nums) - 1)
        else:
            return binarySearch(0, pivot - 1)
                

