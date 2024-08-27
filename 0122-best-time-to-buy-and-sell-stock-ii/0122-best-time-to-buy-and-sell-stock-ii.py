class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        last = prices[0]
        for price in prices:
            if price>=last:
                ans+=(price-last)
            last =  price
        return ans        