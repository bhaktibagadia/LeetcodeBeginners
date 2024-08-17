class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # moore voting algorithm
        n = len(nums)
        el1, el2, cnt1, cnt2 = 1e9+7, 1e9+7, 0, 0
        for num in nums:
            if cnt1 == 0 and el2!=num:
                el1=num
                cnt1=1
            elif cnt2==0 and el1!=num:
                el2=num
                cnt2=1
            elif el1==num:
                cnt1+=1
            elif el2==num:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        ans = []
        if nums.count(el1)>n//3:
            ans.append(el1)
        if nums.count(el2)>n//3:
            ans.append(el2)
        return ans                                
        