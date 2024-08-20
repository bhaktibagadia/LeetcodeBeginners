class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod, maxProd = 1, -1e9
        for num in nums:
            prod*=num
            maxProd = max(maxProd, prod)
            if prod == 0:
                prod = 1
        prod=1
        nums.reverse()
        for num in nums:
            prod*=num
            maxProd = max(maxProd, prod)
            if prod == 0:
                prod = 1
        return maxProd        
