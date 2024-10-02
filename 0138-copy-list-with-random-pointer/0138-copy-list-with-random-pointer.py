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
        prev = dummy = Node(x=0)
        cur, clones = head, {}
        while cur:
            clones[cur] = Node(x=cur.val)
            prev.next = clones[cur]
            prev, cur = clones[cur], cur.next

        while head:
            clones[head].random = clones[head.random] if head.random else None
            head = head.next

        return dummy.next


        