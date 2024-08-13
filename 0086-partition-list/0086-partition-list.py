# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        small_dummy = small = ListNode()
        large_dummy = large = ListNode()
        while cur:
            next = cur.next
            if cur.val < x:
                small.next = cur
                small = small.next
                small.next = None
            else:
                large.next = cur
                large = large.next
                large.next = None
            cur = next
        small.next = large_dummy.next
        return small_dummy.next

        