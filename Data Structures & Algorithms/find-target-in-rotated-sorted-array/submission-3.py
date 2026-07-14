class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        def bs(nums, start, end, target):
            while start <= end:
                mid = start + (end - start)//2
                if nums[mid] > target:
                    end = mid -1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    return mid
            return -1
        
        if target == nums[pivot]:
            return l
        elif nums[pivot] < target and nums[-1] >= target:
            return bs(nums, pivot, len(nums) - 1, target)
        else:
            return bs(nums, 0, pivot - 1, target)
