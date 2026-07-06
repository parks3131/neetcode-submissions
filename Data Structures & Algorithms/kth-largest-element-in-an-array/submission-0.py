class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def quick(l,r):
            p, pivot = l, nums[r]
            for i in range(l,r,1):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                return quick(p+1,r)
            elif p > k:
                return quick(0,p-1)
            else: return nums[p]
        
        return quick(0,len(nums)-1)


        
                


        