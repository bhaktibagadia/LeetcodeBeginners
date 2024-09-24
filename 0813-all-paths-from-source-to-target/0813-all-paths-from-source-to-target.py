class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def rec(i):
            if i==len(graph)-1:
                ans.append(path.copy())
                return
            for j in graph[i]:
                path.append(j)
                rec(j) 
                path.pop()

        path,ans=[],[]
        path.append(0)
        rec(0)
        return ans           