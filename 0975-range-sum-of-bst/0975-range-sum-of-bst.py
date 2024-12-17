# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(node=root):
            if not node: return
            if low <= node.val <= high: self.ans += node.val
            if node.val > low: helper(node.left)
            if node.val < high: helper(node.right)

        self.ans = 0
        helper()
        return self.ans




        