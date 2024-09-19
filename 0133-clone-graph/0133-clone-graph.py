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
        clones, root, queue = {node: Node(node.val, [])}, node, [node]
        while queue:
            next_queue = []
            for node in queue:
                for neighbor in node.neighbors:
                    if neighbor not in clones:
                        clones[neighbor] = Node(neighbor.val, [])
                        next_queue.append(neighbor)
                    clones[node].neighbors.append(clones[neighbor])
            queue = next_queue
        return clones[root]

        