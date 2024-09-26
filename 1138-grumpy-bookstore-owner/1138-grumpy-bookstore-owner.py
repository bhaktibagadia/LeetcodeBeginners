class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxx=0
        for i in range(len(customers)):
            if not grumpy[i]:
                maxx+=customers[i]
        unsatisfied=0
        for i in range(minutes):
            unsatisfied+=(grumpy[i]*customers[i]) 
        ans=unsatisfied
        for i in range(minutes, len(customers)):
            if grumpy[i-minutes]==1:
                unsatisfied-=customers[i-minutes]
            if grumpy[i]==1:
                unsatisfied+=customers[i]
            ans=max(ans, unsatisfied)
        return ans+maxx                       