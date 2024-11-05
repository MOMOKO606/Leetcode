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
        if not head: return head
        dummy = prev = Node(x=0, next=None, random=None)
        cur, clones = head, {}
        while cur:
            clones[cur] = Node(x=cur.val)
            prev.next = clones[cur]
            prev, cur = prev.next, cur.next

        cur = head
        while cur:
            clones[cur].random = clones[cur.random] if cur.random else None
            cur = cur.next

        return clones[head]

        