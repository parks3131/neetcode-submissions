class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(l,r,target,list_):
            while l <= r:
                mid = l+(r-l)//2
                if list_[mid] < target:
                    l = mid + 1
                elif list_[mid] > target:
                    r = mid - 1
                elif list_[mid] == target:
                    return mid
            return -1
        
        if binarySearch(0,len(nums)-1,target,nums) == -1:
            return [-1,-1]
        else:
            pivot = binarySearch(0,len(nums)-1,target,nums)
            left = pivot
            right = pivot
            while left-1 >= 0 and nums[left-1] == target:
                    left-=1 
            while right+1 <= len(nums)-1 and nums[right+1] == target:
                    right+=1

            
            return [left,right]


