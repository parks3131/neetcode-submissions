class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum_array = [0] * len(nums)
        pre_sum_var = 0
        for i in range(0, len(nums),1):
            pre_sum_var+= nums[i]
            self.pre_sum_array[i] = pre_sum_var

    def sumRange(self, left: int, right: int) -> int:
       
        return self.pre_sum_array[right] if left == 0 else self.pre_sum_array[right] - self.pre_sum_array[left - 1] 

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)