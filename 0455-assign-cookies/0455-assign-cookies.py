class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        i, j = 0, 0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                ans+=1
            j+=1
        return ans        