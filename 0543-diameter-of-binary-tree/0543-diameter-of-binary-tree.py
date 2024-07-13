# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findmax(node, maxi):
            if not node:
                return 0
            lh=findmax(node.left, maxi)    
            rh=findmax(node.right, maxi)
            maxi[0]=max(lh+rh, maxi[0])
            return 1+max(lh, rh)
        maxi=[0]
        findmax(root, maxi)
        return maxi[0]    