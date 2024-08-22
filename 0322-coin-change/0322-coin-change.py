class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        def rec(i, amt):
            if i==len(coins)-1:
                if amt%coins[i] == 0:
                    return amt//coins[i]
                else:
                    return 1e9
            if (i, amt) in dp:
                return dp[(i, amt)]
            take = 1e9
            nottake = rec(i+1, amt)
            if amt-coins[i]>=0:
                take = rec(i, amt-coins[i])+1
            dp[(i, amt)] = min(take, nottake)
            return dp[(i, amt)]    

        dp={}
        ans = rec(0, amount)
        if ans>=1e9:
            return -1
        return ans       