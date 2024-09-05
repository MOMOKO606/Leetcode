# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node: return 0
            l, r = helper(node.left), helper(node.right)
            self.ans = max(self.ans, node.val + max(l, r, l + r, 0))
            return max(l, r, 0) + node.val

        self.ans = -inf
        helper(root)
        return self.ans
        