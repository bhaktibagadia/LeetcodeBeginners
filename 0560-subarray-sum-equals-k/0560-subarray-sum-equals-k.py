class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1,count=0,0
        mpp=defaultdict(int)
        mpp[0]=1
        for num in nums:
            sum1+=num
            if sum1-k in mpp:               
                count+=mpp[sum1-k]
            mpp[sum1]+=1         
        return count