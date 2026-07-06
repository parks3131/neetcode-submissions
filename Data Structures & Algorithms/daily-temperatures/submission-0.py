class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        for index,i in enumerate(temperatures):
            j=index+1
            while(j<len(temperatures)):
                if i < temperatures[j]:
                    temperatures[index] = j-index
                    break
                j+=1
                if j == len(temperatures):
                    temperatures[index] = 0

        temperatures[-1]=0
        return temperatures