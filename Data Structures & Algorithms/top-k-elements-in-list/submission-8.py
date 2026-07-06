class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_sets = set(nums)
        nums_sets = sorted(list(nums_sets))
        k_list = []
        dict_lists = {}

        for i in range(len(nums_sets)):
            dict_lists[nums_sets[i]] = nums.count(nums_sets[i])

        sorted_items = sorted(dict_lists.items(),key= lambda x:x[1],reverse = True)
          
        result = [key for key, val in sorted_items[:k]]
        return result
                

        