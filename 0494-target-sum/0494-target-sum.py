class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def rec(i, sol):
            if (i, sol) in dp:
                return dp[(i, sol)]
            if i==len(nums):
                if sol==target:
                    return 1
                return 0
            plus=rec(i+1, sol+nums[i])
            minus=rec(i+1, sol-nums[i])
            dp[(i, sol)]=plus+minus
            return dp[(i, sol)]
        dp={}
        ans = rec(0,0)
        return ans    
