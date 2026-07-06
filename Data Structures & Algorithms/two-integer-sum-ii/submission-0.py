class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_numbers = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dict_numbers:
                return [dict_numbers[target - numbers[i]]+1,i+1]
            dict_numbers[numbers[i]]=i