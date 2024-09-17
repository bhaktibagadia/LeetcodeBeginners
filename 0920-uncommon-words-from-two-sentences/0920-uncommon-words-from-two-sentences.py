class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        mpp = {}
        for s in s1:
            if s in mpp:
                mpp[s]+=1
            else:
                mpp[s]=1
        for s in s2:
            if s in mpp:
                mpp[s]+=1
            else:
                mpp[s]=1
        ans = []        
        for s in mpp.keys():
            if mpp[s]==1:
                ans.append(s)
        return ans        