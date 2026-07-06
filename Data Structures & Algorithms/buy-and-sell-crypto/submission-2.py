class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        diff = 0
        for i in prices:
            mini = min(mini,i)
            if i - mini > 0:
                diff = max(diff, i-mini)
        return diff
        