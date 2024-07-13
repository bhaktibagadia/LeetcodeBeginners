# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxsum(node):
            if not node:
                return 0
            leftsum=max(maxsum(node.left),0)
            rightsum=max(maxsum(node.right),0)
            maxi[0]=max(maxi[0], leftsum+rightsum+node.val)
            return node.val+max(leftsum, rightsum)
        if not root:
            return 0    
        maxi=[-1e9]
        maxsum(root)
        return maxi[0]        