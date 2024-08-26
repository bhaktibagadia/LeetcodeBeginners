class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(i):
            if i>len(nums)-1:
                return 0
            if i==len(nums)-1:
                return nums[-1]
            if dp[i]!=-1:
                return dp[i]
            take = nums[i]+rec(i+2)
            nottake = rec(i+1)
            dp[i] = max(take, nottake)
            return dp[i]
        dp = [-1]*len(nums)    
        ans = rec(0)
        return ans                
