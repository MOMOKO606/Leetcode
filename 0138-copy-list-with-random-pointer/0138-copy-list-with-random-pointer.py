"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur, clones = head, {}
        while cur:
            clones[cur] = Node(cur.val)
            cur = cur.next
        
        dummy = prev = Node(0)
        cur = head
        while cur:
            copyNode = clones[cur]
            copyNode.random = clones[cur.random] if cur.random else None
            prev.next = copyNode
            cur, prev = cur.next, prev.next
        return dummy.next

        