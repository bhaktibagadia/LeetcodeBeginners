class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sums, mult = [], []
        length = len(skill)
        for i in range(length//2):
            sums.append(skill[i]+skill[length-1-i])
            mult.append(skill[i]*skill[length-1-i])
        for i in range(1, len(sums)):
            if sums[i]!=sums[i-1]:
                return -1
        return sum(mult)           