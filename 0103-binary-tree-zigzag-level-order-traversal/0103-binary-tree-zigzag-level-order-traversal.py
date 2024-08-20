# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, count, ans = [root], 1, []
        while queue:
            next_queue = []
            ans = ans + [[node.val for node in queue]] if count & 1 else ans + [[node.val for node in queue[::-1]]]
            for node in queue:
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            queue, count = next_queue, count + 1
        return ans