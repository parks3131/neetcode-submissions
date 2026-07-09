class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index_hash = {}
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1] <= temperatures[i]:
                stack.pop()
            if not stack:
                stack.append(temperatures[i])
                index_hash[temperatures[i]] = i
                temperatures[i] = 0
            else:
                temp = temperatures[i]
                index_hash[temp] = i
                temperatures[i] = index_hash[stack[-1]] - i
                stack.append(temp)
        return temperatures
                
        
            