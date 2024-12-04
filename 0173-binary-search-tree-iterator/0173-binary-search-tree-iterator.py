# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        self.stack, self.root = stack, root
        

    def next(self) -> int:
        self.root = self.stack.pop()
        ans = self.root.val
        self.root = self.root.right
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        return ans
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()