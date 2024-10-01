class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        lowlen = min(len(strs[0]), len(strs[-1]))
        while i<lowlen and strs[0][i]==strs[-1][i]:
            i+=1
        return strs[0][:i]    