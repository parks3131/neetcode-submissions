class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count , res = 0, 0
        for i in nums:
            if count == 0:
                res = i
            count += 1 if res == i else -1
        return res