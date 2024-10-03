# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        ans, queue = [], [root]
        while queue:
            next_queue, largest = [], -inf
            for node in queue:
                largest = max(largest, node.val)
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            queue, ans = next_queue, ans + [largest]
        return ans

        