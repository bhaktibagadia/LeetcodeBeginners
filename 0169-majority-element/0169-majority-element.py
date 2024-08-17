class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore voting algorithm
        el, cnt = 0,0
        for num in nums:
            if cnt == 0:
                cnt = 1
                el = num
            elif el == num:
                cnt+=1
            else:
                cnt-=1
        return el                