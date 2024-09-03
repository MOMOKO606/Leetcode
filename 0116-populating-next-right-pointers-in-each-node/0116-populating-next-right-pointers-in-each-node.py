"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        queue = [root]
        while queue:
            next_queue = []
            for node in queue:
                if node.left: next_queue.append(node.left)
                if node.right: next_queue.append(node.right)
            for i in range(1, len(next_queue)):
                next_queue[i - 1].next = next_queue[i]
            queue = next_queue
        return root

        