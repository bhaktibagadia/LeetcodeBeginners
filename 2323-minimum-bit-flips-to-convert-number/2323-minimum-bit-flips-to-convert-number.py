class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binstart = bin(start)[2:]
        bingoal = bin(goal)[2:]
        maxlen = max(len(binstart), len(bingoal))
        binstart = binstart.zfill(maxlen)
        bingoal = bingoal.zfill(maxlen)
        res = 0
        for start,goal in zip(binstart, bingoal):
            if start!=goal:
                res+=1
        return res        