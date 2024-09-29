class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, maxprofit = 0, 0
        minprice = prices[0]
        for price in prices:
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
            minprice = min(price, minprice)
        return maxprofit    