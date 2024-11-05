# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node=root):
            if not node: return 0
            l, r = max(helper(node.left), 0), max(helper(node.right), 0)
            cur = node.val
            if l > 0: cur += l
            if r > 0: cur += r
            self.ans = max(self.ans, cur)
            return node.val + max(l, r)
        
        self.ans = -inf
        helper()
        return self.ans
        