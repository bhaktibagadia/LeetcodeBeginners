class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 1e9
        maxProfit = -1e9
        for price in prices:
            mini = min(mini, price)
            maxProfit = max(maxProfit, price-mini)
        return maxProfit    