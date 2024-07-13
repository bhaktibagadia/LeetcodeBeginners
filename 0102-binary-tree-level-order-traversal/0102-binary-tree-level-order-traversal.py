# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        q=[root]    
        ans.append([root.val])      
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                node=q.pop(0)
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level.append(node.right.val) 
                    q.append(node.right)
            ans.append(level)
        return ans[:-1]               

            