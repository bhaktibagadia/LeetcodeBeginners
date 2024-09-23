class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        nums.sort(reverse = True)    
        desiredsum = sum(nums)//k
        if nums[0]>desiredsum:
            return False
        dp = [0]*k
        def rec(i):
            if i == len(nums):
                for j in range(k):
                    if dp[j]!=desiredsum:
                        return False
                return True        
            for j in range(k):
                if dp[j]+nums[i]<=desiredsum:
                    dp[j]+=nums[i]
                    if rec(i+1):
                        return True
                    dp[j]-=nums[i]
                if dp[j]==0:
                    return False    
            return False
        return rec(0)                        