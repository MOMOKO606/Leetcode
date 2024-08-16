# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseN(node, n):
            prev, cur = None, node
            while n:
                next = cur.next
                cur.next = prev
                prev, cur = cur, next
                n -= 1
            node.next = cur
            return prev

        dummy = prev = ListNode(next = head)
        cur = head
        count = 0
        while cur:
            count += 1
            if count == left:
                new_head = reverseN(cur, right - left + 1)
                prev.next = new_head
                return dummy.next
            prev, cur = cur, cur.next
        return dummy.next
        