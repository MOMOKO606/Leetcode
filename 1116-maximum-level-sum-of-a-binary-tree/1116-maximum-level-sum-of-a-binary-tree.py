# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue, largest, levels, ans = [root], -inf, 1, 0
        while queue:
            next_queue, total = [], 0
            for node in queue:
                total += node.val
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            if total > largest: largest, ans = total, levels
            queue, levels = next_queue, levels + 1
        return ans


        