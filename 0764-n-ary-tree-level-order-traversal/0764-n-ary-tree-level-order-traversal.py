"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=[]
        q=[]
        level=[]
        if not root:
            return ans
        q.append(root)
        ans.append([root.val])
        while q:
            level=[]
            size=len(q)
            for i in range(size):
                node=q.pop(0)
                for child in node.children:
                    q.append(child)
                    level.append(child.val)
            ans.append(level) 
        return ans[:-1]               