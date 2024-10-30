# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_smaller = prev_smaller = ListNode()
        dummy_larger = prev_larger = ListNode()
        cur = head
        while cur:
            next = cur.next
            if cur.val < x:
                prev_smaller.next = cur
                prev_smaller = cur
                prev_smaller.next = None
            else:
                prev_larger.next = cur
                prev_larger = cur
                prev_larger.next = None
            cur = next
        prev_smaller.next = dummy_larger.next
        return dummy_smaller.next
        