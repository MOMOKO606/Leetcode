# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getPredecessor(node):
            node = node.left
            while node and node.right:
                node = node.right
            return node

        def getSuccessor(node):
            node = node.right
            while node and node.left:
                node = node.left
            return node

        if not root: return root
        if key == root.val:
            if root.left: 
                p = getPredecessor(root)
                root.val = p.val
                root.left = self.deleteNode(root.left, p.val)
            elif root.right:
                s = getSuccessor(root)
                root.val = s.val
                root.right = self.deleteNode(root.right, s.val)
            else: 
                return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

        