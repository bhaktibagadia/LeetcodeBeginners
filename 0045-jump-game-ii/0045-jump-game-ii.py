class Solution:
    def jump(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)
        def rec(i): 
            if i>=len(nums)-1:
                return 0   
            if memo[i] !=-1:
                return memo[i]  
            minjumps = len(nums)+1    
            for ind in range(nums[i], 0, -1):
                jumps = 1+rec(i+ind)
                minjumps = min(minjumps, jumps)    
            memo[i] =  minjumps
            return memo[i]   
        ans = rec(0)
        return ans    


