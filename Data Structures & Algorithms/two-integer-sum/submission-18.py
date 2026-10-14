class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_diff = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_diff:
                return [hash_diff[diff], i]
            hash_diff[num] = i