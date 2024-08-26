# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        flag = 1
        if not root:
            return ans
        q=[]
        q.append(root)
        ans.append([root.val])
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)
            if flag:        
                level.reverse()
                flag = 0
            else:
                flag = 1
            ans.append(level)
        return ans[:-1]           
