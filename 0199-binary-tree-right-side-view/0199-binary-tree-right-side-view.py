# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue, ans = [root], []
        while queue:
            nextQueue = []
            ans.append(queue[-1].val)
            for node in queue:
                if node.left: nextQueue.append(node.left)
                if node.right: nextQueue.append(node.right)
            queue = nextQueue
        return ans
        