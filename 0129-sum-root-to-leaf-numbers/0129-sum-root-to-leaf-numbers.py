# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node=root, seq=""):
            if not node: return
            if not node.left and not node.right: 
                self.ans += int(seq + str(node.val))
                return
            helper(node.left, seq + str(node.val))
            helper(node.right, seq + str(node.val))


        self.ans = 0
        helper()
        return self.ans