class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            temp = []
            dict_for_unique = {}
            for p in res:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,num)
                    if tuple(p_copy) not in dict_for_unique:
                        temp.append(p_copy)
                        dict_for_unique[tuple(p_copy)] = 1
            res = temp.copy()
        return res

        #Since we use dictionary it is constant time for checking
        #In dictionary we can use only immutable key that is why
        #we use tuple.But still IG tuple conversion takes time but yeah

        