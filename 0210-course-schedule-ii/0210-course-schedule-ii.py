class Solution:
    def findOrder(self, V: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(V)]
        for p in prerequisites:
            adj[p[1]].append(p[0])

        indegree=[0]*V
        for i in range(V):
            for ver in adj[i]:
                indegree[ver]+=1

        q=[]
        topo=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)

        while q:
            node=q.pop(0)
            topo.append(node)
            for vertex in adj[node]:
                indegree[vertex]-=1
                if indegree[vertex]==0:
                    q.append(vertex)

        if len(topo)==V:
            return topo
        return []                        