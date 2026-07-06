class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = defaultdict(int)
        for i,num in enumerate(nums):
            if target - num in diff_dict:
                return [diff_dict[target-num],i]
            diff_dict[num] = i
