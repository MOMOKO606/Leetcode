# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node: return [-1, -1]
            [ _, leftMax ] = helper(node.left)
            [ rightMax, _ ] = helper(node.right)
            self.ans = max(self.ans, leftMax + 1, rightMax + 1)
            return [leftMax + 1, rightMax + 1]

        self.ans = -math.inf
        helper(root)
        return self.ans
        