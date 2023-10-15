# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, ans = [root], []
        while queue:
            nextQueue, level = [], []
            for node in queue:
                level.append(node.val)
                if node.left: nextQueue.append(node.left)
                if node.right: nextQueue.append(node.right)
            ans.append(level)
            queue = nextQueue
        return ans

        