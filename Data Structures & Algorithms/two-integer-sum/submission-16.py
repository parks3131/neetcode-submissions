class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_diff = {}
        for i, num in enumerate(nums):
            if target - num not in hash_diff:
                hash_diff[num] = i
            else:
                return [hash_diff[target - num], i]
