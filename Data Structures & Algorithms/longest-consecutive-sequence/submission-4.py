class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums =list(set(nums))
        nums = sorted(nums)
        count = 1
        consec = 1
        for i in range(len(nums)-1):
            if nums[i+1] -nums[i] == 1:
                count+=1
            else:
                consec = max(consec,count)
                count = 1

        return max(consec,count)
            