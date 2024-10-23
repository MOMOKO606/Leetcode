# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def lessThanK(node):
            count = 0
            while node and count < k:
                count, node = count + 1, node.next
            return count < k

        if lessThanK(head): return head
        remain, prev, cur = k, ListNode(), head
        while remain:
            next = cur.next
            cur.next = prev
            prev, cur, remain = cur, next, remain - 1
        head.next = self.reverseKGroup(cur, k)
        return prev


        