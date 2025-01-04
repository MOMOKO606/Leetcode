# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, cur_max):
            if not node: return 
            if node.val >= cur_max:
                self.count += 1
                cur_max = node.val
            helper(node.left, cur_max)
            helper(node.right, cur_max)

        self.count = 0
        helper(root, -inf)
        return self.count

        