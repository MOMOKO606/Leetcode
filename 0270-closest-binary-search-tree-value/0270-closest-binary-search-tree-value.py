# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def helper(node=root):
            if not node: return
            if abs(node.val - target) < self.diff:
                self.diff, self.ans = abs(node.val - target), node.val
            elif abs(node.val - target) == self.diff:
                self.ans = min(self.ans, node.val)
            if node.val > target:
                helper(node.left)
            else:
                helper(node.right)

        self.diff, self.ans = inf, 0
        helper()
        return self.ans
        