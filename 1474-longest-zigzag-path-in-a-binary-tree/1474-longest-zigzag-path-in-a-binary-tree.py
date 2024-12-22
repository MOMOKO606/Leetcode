# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(node=root):
            if not node: return (0, 0)
            _, left_right_side = helper(node.left)
            right_left_side, _ = helper(node.right)
            self.ans = max(self.ans, 1 + left_right_side, 1 + right_left_side)
            return (1 + left_right_side, 1 + right_left_side)

        self.ans = 1
        helper()
        return self.ans - 1 
        