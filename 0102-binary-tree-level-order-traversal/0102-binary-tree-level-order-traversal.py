# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        queue, ans = [root], []
        while queue:
            next_queue, ans = [], ans + [[node.val for node in queue]]
            for node in queue:
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            queue = next_queue
        return ans
        