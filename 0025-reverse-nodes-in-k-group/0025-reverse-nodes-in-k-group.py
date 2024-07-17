# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def has_k_nodes(node):
            count = 0
            while node:
                node, count = node.next, count + 1
            return count >= k

        def reverse_k_nodes(node, k):
            prev, cur = None, node
            while k:
                next = cur.next
                cur.next = prev
                prev, cur, k = cur, next, k - 1
            return prev, node, next

        if not has_k_nodes(head): return head
        new_head, new_tail, next_head = reverse_k_nodes(head, k)
        new_tail.next = self.reverseKGroup(next_head, k)
        return new_head
        