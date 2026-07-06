class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[k] = nums[r]
                k+=1
        return k
        #O(N) the previous one using remove and count is O(N^2)