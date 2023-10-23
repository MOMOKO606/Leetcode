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
        dummy = prev = Node(0)
        old2New, cur = {}, head
        # 1st round
        while cur:
            # Make a copy of current node
            old2New[cur] = Node(cur.val)
            prev.next = old2New[cur]
            prev, cur = prev.next, cur.next
        
        # 2nd round
        cur, prev = head, dummy
        while cur:
            old2New[cur].random = old2New[cur.random] if cur.random else None
            cur = cur.next
        return dummy.next
            
        
        