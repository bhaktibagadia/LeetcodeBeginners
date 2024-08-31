class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1

            return j-i-1   

        start,end=-1,-1
        maxLength=0
        for i in range(len(s)):
            ans_odd=isPalindrome(s,i,i)
            ans_even=isPalindrome(s,i,i+1)
            maxLength=max(ans_odd,ans_even)
            if maxLength>end-start:
                start=i-(maxLength-1)//2
                end=i+maxLength//2

        return s[start:end+1]    

            