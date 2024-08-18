class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numss = sorted(set(nums))
        cnt, maxcount = 1, 1
        
        for i in range(1, len(numss)):
            if numss[i] == numss[i-1] + 1:
                cnt += 1
                maxcount = max(maxcount, cnt)
            else:
                cnt = 1
        
        return maxcount
