# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getLeft(node):
            count = 0
            while node:
                node, count = node.left, count + 1
            return count

        def getRight(node):
            count = 0
            while node:
                node, count = node.right, count + 1
            return count


        if not root: return 0
        l, r = getLeft(root), getRight(root)
        if l == r: return 2 ** l - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        