# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        val = preorder.pop(0)
        k = inorder.index(val)
        return TreeNode(val=val, left=self.buildTree(preorder[:k], inorder[:k]), right=self.buildTree(preorder[k:], inorder[k + 1:]))
        