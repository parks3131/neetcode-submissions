class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0]-cost[0] >= 0:
                return 0
            else:
                return -1
        for i in range(len(gas)):
            Sum = gas[i]
            count = 0
            j = i
            while(count < len(gas)):
                if j == len(gas)-1:
                    if Sum - cost[j] + gas[0] >= 0 :
                        count+=1
                        Sum +=  gas[0] - cost[j]
                        j=-1
                    else:
                        break
                else:
                    if Sum - cost[j] >= 0 :
                        Sum+= gas[j+1] - cost[j]
                        count+=1
                    else:
                        break
                j+=1
            if count == len(gas):
                return i
        return -1