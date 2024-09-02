# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node: return True, 0
            is_left_balanced, left_height = helper(node.left)
            is_right_balanced, right_height = helper(node.right)
            return is_left_balanced and is_right_balanced and abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

        ans = helper(root)
        return ans[0]
        