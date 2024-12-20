# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def helper(node=root):
            if not node: return 0, 0
            left_total, left_count = helper(node.left)
            right_total, right_count = helper(node.right)
            total, count = left_total + right_total + node.val, 1 + left_count + right_count
            self.ans = max(self.ans, total / count)
            return total, count

        self.ans = -inf
        helper()
        return self.ans
        