class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        for i in range(len(prices)-1):
            j=i+1
            while(j<len(prices)):
                if prices[j]-prices[i] > maxprofit:
                    maxprofit = prices[j]-prices[i]
                j+=1
        return maxprofit
        