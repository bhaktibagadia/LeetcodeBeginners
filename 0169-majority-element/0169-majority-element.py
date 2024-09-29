class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 1e9
        cnt = 0
        for num in nums:
            if cnt == 0:
                ans = num
                cnt+=1
            elif num==ans:
                cnt+=1
            else:
                cnt-=1
        return ans            