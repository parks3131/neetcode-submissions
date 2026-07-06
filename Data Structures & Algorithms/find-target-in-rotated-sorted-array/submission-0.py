class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r,nums,target):
            while(l<=r):
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    return mid
            return -1

        if(nums[0]<nums[-1]):
            return binary_search(0,len(nums)-1,nums,target)        
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        if nums[pivot] <= target and target <= nums[-1]:
            return binary_search(pivot,len(nums)-1,nums,target)
        else:
            return binary_search(0,pivot-1,nums,target)


            