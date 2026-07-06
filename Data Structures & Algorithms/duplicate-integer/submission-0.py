class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_sets = set(nums)
        num_lists = list(num_sets)
        return len(num_lists) != len(nums)