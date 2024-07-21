class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        differences=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                differences.append(i)
        if len(differences)==2:
            i, j = differences[0], differences[1]
            return s[i]==goal[j] and goal[i]==s[j]
        elif len(differences)==0:
            return len(set(s))<len(s)
        else:
            return False
        