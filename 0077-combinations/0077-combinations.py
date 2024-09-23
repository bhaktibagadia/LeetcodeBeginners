class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def rec(i, ds):
            if len(ds)==k:
                sol.append(ds[:])
                return
            for ind in range(i, n+1):
                ds.append(ind)
                rec(ind+1, ds)
                ds.pop()
        sol = []        
        rec(1, [])
        return sol                 