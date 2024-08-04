class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraysums=[]
        for i in range(len(nums)):
            temp_sum=0
            for j in range(i, len(nums)):
                temp_sum+=nums[j]
                subarraysums.append(temp_sum)
                
        subarraysums.sort()
        ans=sum(subarraysums[left-1: right])
        return int(ans%(1e9+7))        