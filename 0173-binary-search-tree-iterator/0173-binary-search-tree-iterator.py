# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
       

    def next(self) -> int:
        node = self.stack.pop()
        ans = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return ans


    def hasNext(self) -> bool:
        return not self.stack == []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()