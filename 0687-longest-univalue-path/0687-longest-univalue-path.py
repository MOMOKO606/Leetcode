# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        @cache
        def helper(node=root):
            if not node: return 0     
            l, r = helper(node.left), helper(node.right)
            left = l if node.left and node.val == node.left.val else 0
            right = r if node.right and node.val == node.right.val else 0
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        self.ans = -inf
        helper()
        return self.ans - 1 if self.ans != -inf else 0

        