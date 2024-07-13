# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        q=[root]
        flag=0
        ans.append([root.val])
        while q:
            level=[]
            size=len(q)
            for i in range(size):
                node=q.pop(0)
                if node.left:
                    q.append(node.left) 
                    level.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)
            if flag==1:
                ans.append(level)
            else:
                ans.append(level[::-1])
            flag=not flag
        return ans[:-1]                           