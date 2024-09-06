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
        clones, prev, cur = {}, Node(x=0, next=head), head
        while cur:
            clones[cur] = Node(x=cur.val)
            prev.next = clones[cur]
            cur, prev = cur.next, clones[cur]

        cur = head
        while cur:
            if cur.random: clones[cur].random = clones[cur.random] 
            cur = cur.next

        return clones[head]
        
        