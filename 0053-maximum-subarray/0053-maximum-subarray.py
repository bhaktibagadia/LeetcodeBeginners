class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, summ = -1e9, 0
        for num in nums:
            summ+=num
            maxsum = max(maxsum, summ)
            if summ<0:
                summ = 0
        return maxsum        