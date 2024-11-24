# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(node=root):
            if not node: return
            helper(node.left)
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            helper(node.right)

        self.ans, self.prev = inf, -inf
        helper()
        return self.ans
        