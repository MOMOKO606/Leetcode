# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, sorted_head = ListNode(next=head), head
        cur = head.next
        head.next = None
        while cur:
            next_cur, cur.next = cur.next, None
            next, prev = sorted_head, dummy
            while  next and cur.val < next.val:
                prev, next = next, next.next
            prev.next, cur.next = cur, next
            if next == sorted_head: sorted_head = cur
            cur = next_cur

        prev, cur = None, sorted_head
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        return prev

        