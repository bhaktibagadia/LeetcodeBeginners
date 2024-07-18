class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        summ=0
        sumofnums=sum(nums)
        for i in range(len(nums)):
            summ+=(nums[i]*i)
        maxsum=summ    
        for i in range(len(nums)-1, -1 ,-1):
            summ=summ-((len(nums)-1)*nums[i])+(sumofnums-nums[i])
            maxsum=max(summ, maxsum)
        return maxsum    
