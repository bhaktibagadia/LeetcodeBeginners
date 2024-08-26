class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(i, nums):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            take = nums[i] + rec(i + 2, nums)
            nottake = rec(i + 1, nums)
            dp[i] = max(take, nottake)
            return dp[i]

        n = len(nums)
        if n<=3:
            return max(nums)
        dp = [-1] * (n-1)
        ans1 = rec(0, nums[1:])  
        dp = [-1] * (n-1)
        ans2 = rec(0, nums[:-1])  
        return max(ans1, ans2)

