class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        icecreams=0
        costs.sort()
        for cost in costs:
            if cost>coins:
                break
            icecreams+=1
            coins-=cost
        return icecreams        