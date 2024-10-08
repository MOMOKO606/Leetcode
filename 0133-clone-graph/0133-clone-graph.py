"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        clones, queue, root = {node.val: Node(val=node.val, neighbors=[])}, [node], node
        while queue:
            next_queue = []
            for node in queue:
                for neighbor in node.neighbors:
                    if neighbor.val not in clones:
                        next_queue.append(neighbor)
                        clones[neighbor.val] = Node(val=neighbor.val, neighbors=[])
                    clones[node.val].neighbors.append(clones[neighbor.val])
            queue = next_queue
        return clones[root.val]
        