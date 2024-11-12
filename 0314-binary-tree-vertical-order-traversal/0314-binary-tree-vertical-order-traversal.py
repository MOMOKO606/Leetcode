# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        orders, deque = {}, collections.deque([(root, 0)])
        while deque:
            node, order = deque.popleft()
            orders[order] = orders.get(order, []) + [node.val]
            if node.left: deque.append((node.left, order - 1))
            if node.right: deque.append((node.right, order + 1))
        return [value for _, value in sorted(orders.items(), key=lambda x: x[0])]