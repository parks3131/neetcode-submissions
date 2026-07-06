class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mincostday = prices[0]
        for i in range(1,len(prices)):
            mincostday = min(mincostday, prices[i])
            profit = max(profit, prices[i] - mincostday)
        return profit