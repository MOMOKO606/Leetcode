# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        l, r =  math.inf, math.inf
        if root.left: l = self.minDepth(root.left)
        if root.right: r = self.minDepth(root.right)
        return min(l, r) + 1
        