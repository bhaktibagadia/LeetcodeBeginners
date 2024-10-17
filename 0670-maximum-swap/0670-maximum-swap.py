class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            ind = i
            for j in range(len(s)-1, i, -1):
                if s[ind]<s[j]:
                    ind = j
            if ind!=i and s[i]<s[ind]:
                s[i], s[ind] = s[ind], s[i]
                return int(''.join(s))
        return num                