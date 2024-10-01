class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp = temp[::-1]
        s = ' '.join(temp)
        return s