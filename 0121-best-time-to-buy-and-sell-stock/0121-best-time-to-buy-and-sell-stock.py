class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice, maxprofit = 1e9, 0
        for price in prices:
            minprice = min(minprice, price)
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit    