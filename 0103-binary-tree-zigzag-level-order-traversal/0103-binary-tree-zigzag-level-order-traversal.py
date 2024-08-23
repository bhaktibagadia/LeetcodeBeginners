# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        zigzag = 1
        if not root:
            return ans
        q = [root]
        ans.append([root.val])
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
            if zigzag:
                ans.append(level[::-1])
                zigzag = 0
            else:
                ans.append(level)
                zigzag = 1    
        return ans[:-1]                            