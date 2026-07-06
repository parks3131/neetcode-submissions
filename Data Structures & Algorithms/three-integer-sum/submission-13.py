class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #distinct triplets to give the sum 0
        #[ -4 -1 -1 0 1 2]
        nums.sort()
        curr = 0
        result = []
        while curr < len(nums):
            l, r = curr + 1, len(nums) - 1
            if curr == 0 or curr > 0 and nums[curr] != nums[curr - 1]:
                while l < r:
                    ThreeSum = nums[curr] + nums[l] + nums[r]
                    if ThreeSum > 0:
                        r-=1
                    elif ThreeSum < 0:
                        l+=1
                    else:
                        result.append([nums[curr], nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l - 1] == nums[l]:
                            l+=1
            curr+=1
        return result


            