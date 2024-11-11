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
            self.ans = min(self.ans, node.val, key=lambda x: (abs(x - target), x))
            if target < node.val:
                helper(node.left)
            else:
                helper(node.right)

        self.ans = inf
        helper()
        return self.ans
        