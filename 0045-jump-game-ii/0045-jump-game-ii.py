class Solution:
    def jump(self, nums: List[int]) -> int:
        def rec(i):
            minJumps = 1e9
            if i>=len(nums)-1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            for ind in range(nums[i], 0, -1):
                jump = 1+rec(i+ind)
                minJumps = min(jump,minJumps)
            dp[i] = minJumps
            return dp[i]
        dp = [-1]*len(nums)
        ans = rec(0)
        return ans                