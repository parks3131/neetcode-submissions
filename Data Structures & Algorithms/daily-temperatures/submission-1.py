class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for index,tem in enumerate(temperatures):
            while stack and tem > stack[-1][1]:
                stack_ind,stack_value = stack.pop()
                res[stack_ind] = index-stack_ind
            stack.append([index,tem])
        return res

            