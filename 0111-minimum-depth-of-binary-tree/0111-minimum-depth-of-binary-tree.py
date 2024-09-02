# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root and not root.left and not root.right: return 1
            if not root: return inf
            return 1 + min(helper(root.left), helper(root.right))
        
        ans = helper(root)
        return ans if ans != inf else 0