# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successorVal(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val

        def predecessorVal(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val

        if not root: return root
        if key > root.val: root.right = self.deleteNode(root.right, key)
        elif key < root.val: root.left = self.deleteNode(root.left, key)
        else:
            if not root.right and not root.left: return 
            elif root.right:
                root.val = successorVal(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = predecessorVal(root)
                root.left = self.deleteNode(root.left, root.val)
        return root


        